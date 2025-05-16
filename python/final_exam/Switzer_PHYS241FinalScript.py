import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

from python.read_two_columns_text import read_two_columns_text
from python.calculate_bivariate_statistics import calculate_bivariate_statistics
from generate_matrix import generate_matrix
from python.calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from python.annotate_plot import annotate_plot

# Configuration
FIRST, LAST     = "Ashton", "Switzer"
SHOW            = False
DATA_FILE       = "Si.Fd-3m.GGA-PBEsol.volumes_energies.dat"
POTENTIAL_NAME  = 'square'       #Chat GPT (o4-mini-high "how can I edit this code to put my name in the code without
GRID_POINTS, PARAMETER = 100, 5   # writing it all over the place?

#ChatGPT o4-mini-high "how do I implement the separate file I made to convert units into my main code? Original way
#wasn't working"
def convert_units(values, from_u, to_u):
    bohr_to_ang = 0.529177210903
    ryd_to_eV   = 13.605693009
    eVA3_to_GPa = 160.21766208
    if from_u=='bohr^3/atom' and to_u=='Å^3/atom':
        factor = bohr_to_ang**3
    elif from_u=='rydberg/atom' and to_u=='eV/atom':
        factor = ryd_to_eV
    elif from_u=='rydberg/bohr^3' and to_u=='GPa':
        factor = ryd_to_eV/(bohr_to_ang**3)*eVA3_to_GPa
    else:
        raise ValueError(f"Unsupported conversion: {from_u}→{to_u}")
    return np.array(values) * factor


def annotate(ax, metadata):
    today = datetime.today().date().isoformat()
    info = {f"Created by {FIRST} {LAST} ({today})":
            {'position':[0.01,0.01], 'alignment':['left','bottom'], 'fontsize':8}}
    info.update(metadata)
    plt.sca(ax)
    annotate_plot(info)


def analyze(filename, display_graph=False):
    # Parse metadata
    chem, sym, acr = filename.split('.')[:3]
    # Load and validate data
    data = read_two_columns_text(str(Path(__file__).parent / filename))
    if data.ndim!=2 or data.shape[1]<2:
        raise ValueError(f"Expected data shape (N,2), got {data.shape}")
    V, E = data[:,0], data[:,1]
    if sym=='Fd-3m':
        E = E/2

    # Bivariate statistics
    stats = calculate_bivariate_statistics(np.vstack([V,E]))

    # Quadratic EOS fit (no SciPy)
    # Fit E(V) = a*V^2 + b*V + c
    # Using numpy.polyfit gives highest-power-first coefficients
    p2, p1, p0 = np.polyfit(V, E, 2)  # p2*V^2 + p1*V + p0
    # Build fit curve
    V_fit = np.linspace(V.min(), V.max(), 200)
    E_fit = p2*V_fit**2 + p1*V_fit + p0
    # Derive EOS-like params
    V0 = -p1/(2*p2)
    K0 = 2*p2*V0
    E0 = p2*V0**2 + p1*V0 + p0
    K0p = 4.0  # placeholder derivative

    #convert units
    V_A3      = convert_units(V, 'bohr^3/atom', 'Å^3/atom')
    E_eV      = convert_units(E, 'rydberg/atom', 'eV/atom')
    X_A3      = convert_units(V_fit, 'bohr^3/atom', 'Å^3/atom')
    E_fit_eV  = convert_units(E_fit, 'rydberg/atom', 'eV/atom')
    V0_A3     = convert_units(V0, 'bohr^3/atom', 'Å^3/atom')
    K0_GPa    = convert_units(K0, 'rydberg/bohr^3', 'GPa')

    # Plot EOS (quadratic)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(X_A3, E_fit_eV, 'k-', label='Quadratic Fit')
    ax.scatter(V_A3, E_eV, color='C0', label='DFT data')
    ax.axvline(V0_A3, linestyle='--', color='gray', label=f'V₀={V0_A3:.2f} Å³')
    ax.set_xlim(V_A3.min()*0.9, V_A3.max()*1.1)
    ax.set_ylim(E_eV.min()-0.1, E_eV.max()+0.1)
    ax.set_xlabel(r'$V$ [Å³/atom]')    #ChatGPT o4-mini-high "Why isn't the equations_of_state function working in my code?
    ax.set_ylabel(r'$E$ [eV/atom]')
    ax.set_title(f"Quadratic EOS for {chem} ({acr})")
    annotate(ax, {
        f"Symmetry: {sym}": {'position':[0.01,0.92],'alignment':['left','top'],'fontsize':10},
        f"Bulk modulus: {K0_GPa:.1f} GPa": {'position':[0.01,0.88],'alignment':['left','top'],'fontsize':10},
        f"K₀': {K0p:.2f}": {'position':[0.01,0.84],'alignment':['left','top'],'fontsize':10},
        f"Energy range: {stats[4]:.2f}–{stats[5]:.2f} eV": {'position':[0.01,0.80],'alignment':['left','top'],'fontsize':10}
    })
    if display_graph:
        plt.show()
    else:
        plt.savefig(f"{LAST}.{chem}.{sym}.{acr}.EOS.png", dpi=300)
    plt.close(fig)

    # Plot square‑well potential
    xmin, xmax = -10, 10
    x = np.linspace(xmin, xmax, GRID_POINTS)
    dx = (xmax - xmin)/(GRID_POINTS - 1)
    prefac = 1.0/(2*dx**2)
    H = generate_matrix(xmin, xmax, GRID_POINTS, POTENTIAL_NAME, PARAMETER)
    Vx = np.diag(H) - 2*prefac
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(x, Vx, drawstyle='steps-mid')
    ax.set_ylim(-0.1, Vx.max()*1.1)
    ax.set_xlabel('x [a.u.]')
    ax.set_ylabel('V(x) [a.u.]')
    ax.set_title('Square‑Well Potential')
    annotate(ax, {})
    if display_graph:
        plt.show()
    else:
        plt.savefig(f"{LAST}.square.Potential.png", dpi=300)
    plt.close(fig)

    # Wavefunctions
    H = generate_matrix(xmin, xmax, GRID_POINTS, POTENTIAL_NAME, PARAMETER)
    vals, vecs = calculate_lowest_eigenvectors(H, 3)
    x = np.linspace(xmin, xmax, GRID_POINTS)
    for i, (val, psi) in enumerate(zip(vals, vecs)):
        psi = psi if psi.max()>abs(psi.min()) else -psi
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(x, psi, label=fr"$\psi_{i}, E_{i}={val:.3f}\,\mathrm{{a.u.}}$")
        ax.axhline(0, color='k')
        ax.set_ylim(-2*abs(psi).max(), 2*abs(psi).max())
        ax.set_xlabel(r'$x$ [a.u.]')
        ax.set_ylabel(r'$\psi_n(x)$ [a.u.]')
        ax.set_title('Wavefunctions for a Square‑Well Potential')
        ax.legend()
        annotate(ax, {})
        if display_graph:
            plt.show()
        else:
            plt.savefig(f"{LAST}.square.Eigenvector{i}.png", dpi=300)
        plt.close(fig)

if __name__=='__main__':
    analyze(DATA_FILE, display_graph=SHOW)

#Ran into some issues earlier where I was making the graph harmonic instead of square. I was completely incorrectly
#using the equations_of_state file, so I hope that it's all fixed and good now.

#Needed ChatGPT o4-mini-high to help me fix my code to not use scipy. It's not downloaded on my computer, and when I
#tried to download it, it wouldn't let me.

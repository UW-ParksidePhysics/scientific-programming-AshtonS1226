import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

from python.read_two_columns_text import read_two_columns_text
from python.calculate_bivariate_statistics import calculate_bivariate_statistics
from python.calculate_quadratic_fit import calculate_quadratic_fit
from equations_of_state import fit_equation_of_state
from generate_matrix import generate_matrix
from python.calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from python.annotate_plot import annotate_plot

# Configuration
FIRST, LAST     = "Ashton", "Switzer"
SHOW            = False
DATA_FILE       = "Si.Fd-3m.GGA-PBEsol.volumes_energies.dat"
POTENTIAL_NAME  = 'Square'
GRID_POINTS, PARAMETER = 100, 5


def convert_units(values, from_u, to_u):
    """
    Convert between:
      - bohr^3/atom ↔ Å^3/atom
      - rydberg/atom ↔ eV/atom
      - rydberg/bohr^3 ↔ GPa
    """
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
    """
    Use annotate_plot to add signature and metadata to axis `ax`.
    metadata: dict mapping text→{position, alignment, fontsize}
    """
    today = datetime.today().date().isoformat()
    info = {f"Created by {FIRST} {LAST} ({today})":
            {'position':[0.01,0.01], 'alignment':['left','bottom'], 'fontsize':8}}
    info.update(metadata)
    plt.sca(ax)
    annotate_plot(info)


def analyze(filename, display_graph=False):
    # Parse chemical symbol, symmetry, DFT acronym
    chem, sym, acr = filename.split('.')[:3]
    # Load data
    data = read_two_columns_text(str(Path(__file__).parent / filename))
    # Validate and extract first two columns
    if data.ndim!=2 or data.shape[1]<2:
        raise ValueError(f"Expected data shape (N,2), got {data.shape}")
    V = data[:,0]
    E = data[:,1]
    # Normalize energy per atom if needed
    if sym=='Fd-3m':
        E = E/2

    # Stats. and quadratic fit
    stats = calculate_bivariate_statistics(np.vstack([V,E]))
    a,b,c = calculate_quadratic_fit(np.vstack([V,E]))
    def eos_curve(x): return a*x**2 + b*x + c
    V0 = -b/(2*a)
    K0 = 2*a*V0

    # Unit conversions
    V_A3  = convert_units(V, 'bohr^3/atom', 'Å^3/atom')
    E_eV  = convert_units(E, 'rydberg/atom', 'eV/atom')
    X     = np.linspace(V.min(), V.max(), 200)
    X_A3  = convert_units(X, 'bohr^3/atom', 'Å^3/atom')
    E_fit = convert_units(eos_curve(X), 'rydberg/atom', 'eV/atom')
    V0_A3 = convert_units(V0, 'bohr^3/atom', 'Å^3/atom')
    K0_GPa= convert_units(K0, 'rydberg/bohr^3', 'GPa')

    #Plot EOS
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(X_A3, E_fit, 'k-', label='Fit')
    ax.scatter(V_A3, E_eV, color='C0', label='DFT data')
    ax.axvline(V0_A3, linestyle='--', color='gray', label=f'V₀={V0_A3:.2f}')
    ax.set_xlim(V_A3.min()*0.9, V_A3.max()*1.1)
    ax.set_ylim(E_eV.min()-0.1, E_eV.max()+0.1)
    ax.set_xlabel(r'$V$ [Å³/atom]')
    ax.set_ylabel(r'$E$ [eV/atom]')
    ax.set_title(f"Quadratic EOS for {chem} ({acr})")
    annotate(ax, {
        f"Symmetry: {sym}": {'position':[0.01,0.92],'alignment':['left','top'],'fontsize':10},
        f"Bulk modulus: {K0_GPa:.1f} GPa": {'position':[0.01,0.88],'alignment':['left','top'],'fontsize':10},
        f"E range: {stats[4]:.2f}-{stats[5]:.2f} eV": {'position':[0.01,0.84],'alignment':['left','top'],'fontsize':10}
    })
    if display_graph: plt.show()
    else: plt.savefig(f"{LAST}.{chem}.{sym}.{acr}.EOS.png", dpi=300)
    plt.close(fig)

    # Wavefunction plots
    # Fixed generate_matrix call signature: xmin, xmax, n_points, potential_name, parameter
    H = generate_matrix(-10, 10, GRID_POINTS, POTENTIAL_NAME, PARAMETER)
    vals, vecs = calculate_lowest_eigenvectors(H, 3)
    x = np.linspace(-10,10,GRID_POINTS)
    for i,(val,psi) in enumerate(zip(vals,vecs)):
        psi = psi if psi.max()>abs(psi.min()) else -psi
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(x, psi, label=fr"$\psi_{i}$, $E_{i}$={val:.3f} a.u.")
        ax.axhline(0, color='k')
        ax.set_ylim(-2*abs(psi).max(),2*abs(psi).max())
        ax.set_xlabel(r'$x$ [a.u.]')
        ax.set_ylabel(r'$\psi_n(x)$ [a.u.]')
        ax.set_title(f"Wavefunctions for a {POTENTIAL_NAME} Potential")
        ax.legend()
        annotate(ax, {})
        if display_graph: plt.show()
        else: plt.savefig(f"{LAST}.{POTENTIAL_NAME}.Eigenvector{i}.png", dpi=300)
        plt.close(fig)

if __name__=='__main__':
    analyze(DATA_FILE, display_graph=SHOW)




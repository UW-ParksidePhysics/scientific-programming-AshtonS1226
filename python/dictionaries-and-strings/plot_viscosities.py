import numpy as np
import matplotlib.pyplot as plt

def parse_viscosity_data(filename):
    """Reads viscosity data from file into a nested dictionary."""
    viscosity_data = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().startswith('#') or not line.strip():
                continue
            parts = line.split()
            gas = parts[0].lower()
            C = float(parts[1])
            T0 = float(parts[2])
            mu0 = float(parts[3])
            viscosity_data[gas] = {
                'viscosity': C,
                'reference_temperature': T0,
                'reference_viscosity': mu0
            }
    return viscosity_data

def calculate_viscosity(T, gas, viscosity_data):
    """Computes μ(T) for a given gas and temperature(s)."""
    C = viscosity_data[gas]['viscosity']
    T0 = viscosity_data[gas]['reference_temperature']
    mu0 = viscosity_data[gas]['reference_viscosity']
    factor = ((T0 - C) / (T + C)) * ((T / T0) ** 1.5)
    return mu0 * factor

if __name__ == '__main__':
    data_file = 'viscosity_of_gases.dat'
    viscosity_data = parse_viscosity_data(data_file)

    gases = ['air', 'carbon', 'hydrogen']
    T = np.linspace(223, 373, 200)

    plt.figure(figsize=(8, 6))

    for gas in gases:
        label = gas if gas != 'carbon' else 'carbon dioxide'
        mu = calculate_viscosity(T, gas, viscosity_data)
        plt.plot(T, mu, label=label.title())

    plt.xlabel('Temperature (K)')
    plt.ylabel('Viscosity μ(T) (Pa·s)')
    plt.title('Viscosity of Gases vs Temperature')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
import numpy as np

def gaussian(x):
    """vectorized gaussian function for Numpy array input"""
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

if __name__ == '__main__':
    x_values = np.linspace(-4, 4, 41)
    y_values = gaussian(x_values)

    print(f"{'x':>8} {'g(x)':>12}")
    print("-" * 20)

    for x, y in zip(x_values, y_values):
        print(f"{x:8.2f} {y:12.5f}")
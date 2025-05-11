import numpy as np
import math

def gaussian(position):
    """computes th value of the Gaussian function at a given position."""
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position ** 2)

if __name__ == '__main__':
    x_values = np.linspace(-4, 4, 41)
    y_values = np.zeros_like(x_values)

    for i in range(len(x_values)):
        y_values[i] = gaussian(x_values[i])

    #print header
    print(f"{'x':>8} {'g(x)':>12}")
    print("-" * 20)

    for x, y in zip(x_values, y_values):
        print(f"{x:8.2f} {y:12.5f}")
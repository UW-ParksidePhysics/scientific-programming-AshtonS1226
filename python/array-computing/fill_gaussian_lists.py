import numpy as np
import math

def gaussian(position):
    """computes the value of the gaussian function at a given position"""
    return(1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position ** 2)

if __name__ == '__main__':
    positions = np.linspace(-4, 4, 41)
    gaussian_values = [gaussian(x) for x in positions]

    print(f"{'x':>8} {'g(x)}':>12}")
    print("-" * 20)

    for x, g in zip(positions, gaussian_values):
        print(f"{x:8.2f} {g:12.5f}")


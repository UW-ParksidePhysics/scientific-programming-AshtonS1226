import numpy as np
import matplotlib.pyplot as plt
import math

def gaussian(x):
    """Compute Gaussian function g(x) = (1/sqrt(2π)) * exp(-0.5 * x^2)"""
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

if __name__ == '__main__':
    x_values = np.linspace(-4, 4, 41)
    y_values = [gaussian(x) for x in x_values]

    plt.plot(x_values, y_values, 'b-', label='g(x)')
    plt.title("Plot of the Gaussian Function")
    plt.xlabel("x")
    plt.ylabel("g(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
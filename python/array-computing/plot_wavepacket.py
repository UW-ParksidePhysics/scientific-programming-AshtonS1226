import numpy as np
import matplotlib.pyplot as plt

def wave_packet(x, t, alpha, f, k, omega):
    """Compute wave packet function for given parameters."""
    return np.exp(-((alpha * x - f * t) ** 2)) * np.sin(k * x - omega * t)


if __name__ == '__main__':
    # Constants
    t = 0
    f = 3
    k = 3 * np.pi
    omega = 3 * np.pi
    alphas = [0.5, 1, 2]

    x = np.linspace(-4, 4, 500)

    plt.figure(figsize=(8, 6))
    for alpha in alphas:
        y = wave_packet(x, t, alpha, f, k, omega)
        plt.plot(x, y, label=f'α = {alpha}')

    plt.title("Wave Packet at t = 0 for different α values")
    plt.xlabel("x")
    plt.ylabel("f(x, 0)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
"""
The file I made here defines a plotting utility and then tests it on a practice dataset. It's reusable and overlays(x,y)
data and a smooth curve model in one function, plus a quick example showing it on a simple quadratic.
"""

__author__ = "Ashton Switzer"

import matplotlib.pyplot as plt
import numpy as np

def plot_data_with_fit(
    data: np.ndarray,
    fit_curve: np.ndarray,
    data_format: str = 'o',
    fit_format: str = ''
) -> list:
    x_data, y_data = data
    x_fit,  y_fit  = fit_curve

    # Plot scatter and fitted curve
    line_data, = plt.plot(x_data, y_data, data_format)
    line_fit,  = plt.plot(x_fit,  y_fit,  fit_format)


    return [line_data, line_fit]

if __name__ == "__main__":
    xs = np.array([-2, -1, 0, 1, 2])
    ys = xs**2
    data = np.vstack([xs, ys])

    #make grid look better
    x_fine = np.linspace(-2, 2, 100)
    y_fine = x_fine**2
    fit_curve = np.vstack([x_fine, y_fine])

    # Chat GPT, o4-mini-high, "How do I change color of "x's" to be more visible against curve?"
    # Plot with 'x' markers for data and dashed line for fit
    lines = plot_data_with_fit(data, fit_curve, data_format='x', fit_format='--')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data and Quadratic Fit")
    plt.legend(lines, ["data points", "fit curve"])
    plt.show()
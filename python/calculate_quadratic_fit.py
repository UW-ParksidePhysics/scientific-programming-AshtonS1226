"""
This allows us to fit a parabola to any two row (x,y) dataset. Ideally you could import calculate_quadratic_fit, give it
an array, and it gives you back three numbers you need to construct a best-fit parabola. How? I'm not entirely sure yet.
One problem at a time.
"""

__author__ = "Ashton Switzer"

import numpy as np

def calculate_quadratic_fit(data: np.ndarray) -> np.ndarray:
    # Check that we got exactly two rows and more than one column
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError(f"Expected shape (2, M) with M>1, got {data.shape}.")

    x, y = data
    # polyfit returns [c2, c1, c0], so we reverse it
    coeffs = np.polyfit(x, y, 2)[::-1]
    return coeffs


if __name__ == "__main__":
    xs = np.linspace(-1, 1)
    ys = xs**2
    data = np.vstack([xs, ys])

    coeffs = calculate_quadratic_fit(data)
    print(f"coeffs = {coeffs}")
    print("expected = [0.0, 0.0, 1.0]")
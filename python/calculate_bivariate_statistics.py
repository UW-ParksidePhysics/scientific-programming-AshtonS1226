"""
This file inputs a 2xM array where the first row is x values and the second row is y values with M>1. It also checks
that you actually passed a 2xM array. It computes the mean of the y values, standard deviation of y values, min and max
of x values, and min and max of y values.
"""

__author__ = "Ashton Switzer"

import numpy as np
# Couldn't use scipy. Wouldn't work because I didn't have scipy downloaded on my computer.
# When I tried to download it, it kept giving me an error. Used a workaround.
def calculate_bivariate_statistics(data: np.ndarray) -> np.ndarray:
    # Validate dimensions
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError(f"Data must have shape (2, M) with M>1, got {data.shape}.")

    x, y = data

    # Computes mean and standard deviation using NumPy
    mean_y = np.mean(y)
    std_y  = np.std(y)  # default ddof=0 for population

    # Compute min/max
    min_x, max_x = np.min(x), np.max(x)
    min_y, max_y = np.min(y), np.max(y)

    return np.array([mean_y, std_y, min_x, max_x, min_y, max_y])


if __name__ == "__main__":
    # Test: symmetric array centered at zero: [-2, -1, 0, 1, 2]
    arr = np.array([-2, -1, 0, 1, 2], dtype=float)
    data = np.vstack([arr, arr])
    stats_out = calculate_bivariate_statistics(data)
    print(f"stats_out = {stats_out}")
    # Expected: [0.0, sqrt(2)=1.41421356..., -2.0, 2.0, -2.0, 2.0]
    expected = np.array([0.0, np.sqrt(2), -2.0, 2.0, -2.0, 2.0])
    print(f"expected  = {expected}")
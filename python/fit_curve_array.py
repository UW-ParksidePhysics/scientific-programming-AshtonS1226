"""
This file turns quadratic-fit coefficients into a smooth curve array. The test block generates five points from x = -2
to 2, which then prints out the resulting curve array and the expected [[-2,-1,0,1,2];[4,1,0,1,4] to make sure it's
correct.
"""

__author__ = "Ashton Switzer"

import numpy as np

def fit_curve_array(
    quadratic_coefficients: np.ndarray,
    minimum_x: float,
    maximum_x: float,
    number_of_points: int = 100
) -> np.ndarray:
    # Validate inputs
    if maximum_x < minimum_x:
        raise ArithmeticError(f"maximum_x ({maximum_x}) must be >= minimum_x ({minimum_x}).")
    if number_of_points <= 2:
        raise IndexError(f"number_of_points ({number_of_points}) must be > 2.")

    # Create N points between minimum_x and maximum_x
    x = np.linspace(minimum_x, maximum_x, number_of_points)
    # Evaluate the polynomial c0 + c1*x + c2*x^2 at each x
    # numpy.polynomial.polynomial.polyval expects coeffs [c0, c1, c2]
    y = np.polynomial.polynomial.polyval(x, quadratic_coefficients)

    return np.vstack([x, y])


if __name__ == "__main__":
    # Quick test: y = x^2
    coeffs = np.array([0, 0, 1], dtype=float)
    curve = fit_curve_array(coeffs, minimum_x=-2.0, maximum_x=2.0, number_of_points=5)
    print("curve =")
    print(curve)
    # Expected x = [-2., -1., 0., 1., 2.]
    #          y = [ 4.,  1., 0.,  1.,  4.]
    expected_x = np.array([-2., -1., 0., 1., 2.])
    expected_y = expected_x**2
    expected = np.vstack([expected_x, expected_y])
    print("expected =")
    print(expected)
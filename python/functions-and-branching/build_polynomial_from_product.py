import numpy as np

def construct_polynomial_from_roots(x, roots):
    """computes value of polynomail at specific value of x"""

    p = 1
    for r in roots:
        p *= (x - r)
    return p

def test_construct_polynomial_from_roots():
    """ Tests function with a known root set"""

    roots = [1, 2]
    test_points = [0, 1, 2, 3]
    expected = [2, 0, 0, 2]

    for x, exp_val in zip(test_points, expected):
        result = construct_polynomial_from_roots(x, roots)
        print(f"p({x}) = {result}, expected = {exp_val}, error = {abs(result - exp_val)}")

if __name__ == "__main__":
    test_construct_polynomial_from_roots()
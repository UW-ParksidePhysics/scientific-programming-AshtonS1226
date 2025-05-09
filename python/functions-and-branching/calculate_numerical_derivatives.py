import math

from matplotlib.transforms import interval_contains


def calculate_difference_quotient(function, position, interval=1e-5):
    """Approximates derivative of function at specific position"""

    h = interval
    return(function(position + h) - function(position - h)) / (2 * h)

def test_difference_quotient():
    """ Tests difference quotient using quadratic function"""

    def quadratic(x):
        return 3 * x**2 + 2 * x + 1

    def exact_derivative(x):
        return 6 * x + 2

    x = 1.0
    approx = calculate_difference_quotient(quadratic, x)
    exact = exact_derivative(x)
    error = abs(approx - exact)

    print(f"Quadratic Test at x = {x}: Approx = {approx}, Exact = {exact}, Error = {error}")

def run_tests():
    h = 0.01

    # 1. f(x) = e^x at x = 0
    f1 = lambda x: math.exp(x)
    df1 = lambda x: math.exp(x)
    x1 = 0
    approx1 = calculate_difference_quotient(f1, x1, h)
    exact1 = df1(x1)
    print(f"f(x)=e^x at x=0: Approx = {approx1}, Exact = {exact1}, Error = {abs(approx1 - exact1)}")

    # 2. f(x) = e^(-2x^2) at x = 0
    f2 = lambda x: math.exp(-2 * x ** 2)
    df2 = lambda x: -4 * x * math.exp(-2 * x ** 2)
    x2 = 0
    approx2 = calculate_difference_quotient(f2, x2, h)
    exact2 = df2(x2)
    print(f"f(x)=e^(-2x^2) at x=0: Approx = {approx2}, Exact = {exact2}, Error = {abs(approx2 - exact2)}")

    # 3. f(x) = cos(x) at x = 2π
    f3 = lambda x: math.cos(x)
    df3 = lambda x: -math.sin(x)
    x3 = 2 * math.pi
    approx3 = calculate_difference_quotient(f3, x3, h)
    exact3 = df3(x3)
    print(f"f(x)=cos(x) at x=2π: Approx = {approx3}, Exact = {exact3}, Error = {abs(approx3 - exact3)}")

    # 4. f(x) = ln(x) at x = 1
    f4 = lambda x: math.log(x)
    df4 = lambda x: 1 / x
    x4 = 1
    approx4 = calculate_difference_quotient(f4, x4, h)
    exact4 = df4(x4)
    print(f"f(x)=ln(x) at x=1: Approx = {approx4}, Exact = {exact4}, Error = {abs(approx4 - exact4)}")


if __name__ == "__main__":
    test_difference_quotient()
    run_tests()
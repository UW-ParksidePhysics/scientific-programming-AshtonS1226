import math

def compute_smoothed_heaviside(position, epsilon=0.01):
    """ compute the smoothed heaviside step function H_epsilon(x)"""
    x = position
    e = epsilon

    if x < -e:
        return 0
    elif -e <= x <= e:
        return 0.5 + x / (2 * e) + (1 / (2 * math.pi)) * math.sin(math.pi * x / e)
    else:
        return 1

def test_smoothed_heaviside():
    """Test the compute_smoothed_heaviside function for different x values"""
    epsilon = 0.01
    test_values = [-0.02, -0.01, 0, 0.01, 0.02]

    for x in test_values:
        result = compute_smoothed_heaviside(x, epsilon)
        print(f"H_eps({x}) = {result}")

if __name__ == "__main__":
    test_smoothed_heaviside()
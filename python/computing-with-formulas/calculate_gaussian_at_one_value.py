import math

# The variables that we had
mean = 0  # m
standard_deviation = 2  # s    Also had to look up what value meant in equation
input_value = 1  # x

# Gaussian function. Used ChatGPT to figure out how to write in Python
gaussian_value = (1 / (math.sqrt(2 * math.pi) * standard_deviation)) * \
                 math.exp(-((input_value - mean) ** 2) / (2 * standard_deviation ** 2))

# Print the inputs and the output
print(f"Mean (m): {mean}")
print(f"Standard Deviation (s): {standard_deviation}")
print(f"Input Value (x): {input_value}")
print(f"Gaussian Function Value: {gaussian_value:.6f}")

maximum_integer = 100

sum_using_loop = 0

for i in range(1, maximum_integer + 1):
    sum_using_loop += i

sum_using_formula = (maximum_integer * (maximum_integer + 1)) // 2

print(f"Sum using for loop: {sum_using_loop}")
print(f"Sum using formula: {sum_using_formula}")
print(f"Do the results match {'Yes' if sum_using_loop == sum_using_formula else 'No'}")
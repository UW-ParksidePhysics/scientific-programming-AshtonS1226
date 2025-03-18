# Initial amount
P = 1000

# Annual interest rate
r = 0.043

# Time period
n = 3  # years

#Equation for n years, but here, we set n equal to 3 years
A = P * (1 + r)**(n)

# Print the results
print(f"Initial amount: ${P:.2f}")
print(f"Annual interest rate: {r * 100:.2f}%")
print(f"Amount after {n} years: ${A:.2f}")
# A little messy, but it got the job done
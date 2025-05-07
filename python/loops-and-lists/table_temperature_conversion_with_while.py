# tavle header

print(f"{'degree F':>5} {'degree C':>7}")

fahrenheit = 0

# loop from zero to 100
while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:>5} {celsius:7.2f}")
    fahrenheit += 10
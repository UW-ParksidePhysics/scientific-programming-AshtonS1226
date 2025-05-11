import sys #so says chat gpt (ChatGPT 4o)

def convert_fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_fahrenheit_temperature_to_celsius_from_input.py <temperature_in_fahrenheit>")
    else:
        try:
            fahrenheit = float(sys.argv[1])
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}degreeF is {celsius:.2f}degreeC")
        except ValueError:
            print("Please enter a valid numeric temperature.")

# Again, come back, I can't get it to work right
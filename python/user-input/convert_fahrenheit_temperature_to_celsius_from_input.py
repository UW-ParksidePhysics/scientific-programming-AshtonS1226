def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == "__main__":
    try:
        fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
        celsius_output = fahrenheit_to_celsius(fahrenheit_input)
        print(f"{fahrenheit_input:.2f}degreeF is {celsius_output:.2f}degreeC")
    except ValueError:
        print("Please enter a valid number.")


# Come back to it, can't figure out how to get it to work


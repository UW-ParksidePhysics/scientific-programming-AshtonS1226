import sys

def convert_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    try:
        fahrenheit = float(sys.argv[1])
        celsius = convert_f_to_c(fahrenheit)
        print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")
    except IndexError:
        print("Error: Missing temperature argument.\nUsage: python convert_temperature_from_command_line.py <temperature_in_fahrenheit>")
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")

# Note: come back and fix code so that all lines are within pycharm boundary
# Used ChatGPT to fix bottom half of code (ChatGPT 4o)

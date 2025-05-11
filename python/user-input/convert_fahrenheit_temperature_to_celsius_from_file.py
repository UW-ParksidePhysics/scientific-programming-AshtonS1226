def convert_fahrenheit_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def read_temperature_from_file(filename):
    """Reads the Fahrenheit temperature from a file and returns it as a float."""
    with open(filename, 'r') as file:
        lines = file.readlines()      # Second half of this function was made using ChatGPT 
        if len(lines) < 3:
            raise ValueError("File does not contain enough lines.")
        words = lines[2].split()
        return float(words[2])  # third word is the numeric temperature

if __name__ == '__main__':
    try:
        filename = 'temperature_data.txt'
        fahrenheit = read_temperature_from_file(filename)
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")
    except FileNotFoundError:
        print("The file was not found.")
    except (IndexError, ValueError):
        print("The file format is incorrect or data is invalid.")
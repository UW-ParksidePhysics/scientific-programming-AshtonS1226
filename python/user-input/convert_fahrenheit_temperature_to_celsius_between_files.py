def convert_f_to_c(f):
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    with open('temperature_data.txt', 'r') as infile:
        lines = infile.readlines()[2:]  # skip the header lines

    fahrenheit = [float(line.split()[2]) for line in lines if line.startswith('Fahrenheit')]
    celsius = [convert_f_to_c(f) for f in fahrenheit]

    with open('converted_temperatures.txt', 'w') as outfile:
        outfile.write("Fahrenheit (°F)\tCelsius (°C)\n")
        for f, c in zip(fahrenheit, celsius):
            outfile.write(f"{f:.1f}\t\t{c:.1f}\n")
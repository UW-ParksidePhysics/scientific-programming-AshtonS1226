def parse_constants_file(filename):
    """Reads a file of physical constants and returns a dictionary of names to values."""
    constants = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Skip blank lines and comments
            parts = line.split()
            name = " ".join(parts[:-2])  # Al but last two parts
            value = float(parts[-2])     # Second to last is  value
            constants[name] = value
    return constants

if __name__ == '__main__':
    constants = parse_constants_file('constants.txt')
    for name, value in constants.items():
        print(f"{name}: {value}")
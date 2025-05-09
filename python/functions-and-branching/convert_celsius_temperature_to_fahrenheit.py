def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    """Converts Fahrenheit temperature to Celsius """

    return (5 / 9) * (fahrenheit_temperature - 32)


def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    """Converts Celsius temperature to Fahrenheit """
    return (9 / 5) * celsius_temperature + 32


def run_temperature_conversion_tests():
    """
    Tests the conversion functions using three known temperatures:
    1. Freezing point of water (0 °C)
    2. Room temperature (21 °C)
    3. Boiling point of water (100 °C)
    """
    test_celsius_values = [0, 21, 100]
    print(f"{'Celsius':>10} {'Fahrenheit':>12} {'Back to Celsius':>18} {'Error':>10}")
    print("-" * 50)

    for c in test_celsius_values:
        f = convert_celsius_temperature_to_fahrenheit(c)
        c_back = convert_fahrenheit_temperature_to_celsius(f)
        error = abs(c - c_back)
        print(f"{c:10.2f} {f:12.2f} {c_back:18.2f} {error:10.6f}")


if __name__ == "__main__":
    run_temperature_conversion_tests()
densities = {
    "iron": 7.874,  # g/cm^3
    "air": 0.001225,  # g/cm^3
    "gasoline": 0.755,  # g/cm^3
    "ice": 0.9167,  # g/cm^3
    "human_body": 1.062,  # g/cm^3
    "silver": 10.49,  # g/cm^3
    "platinum": 21.45  # g/cm^3
}

volume = 1000  # cm^3

masses = {substance: density * volume for substance, density in densities.items()}
#AI software used to figure out some of the lines above

print("Mass of 1 liter of each substance (in grams):")
for substance, mass in masses.items():
    print(f"{substance.capitalize()}: {mass:.2f} g")

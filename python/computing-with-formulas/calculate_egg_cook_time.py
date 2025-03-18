import math

# Constants
density = 1.038  # g/cm³
specific_heat_capacity = 3.7  # J/g°C
thermal_conductivity = 5.4e-3  # W/cm°C
boiling_water_temp = 100  # °C
target_temp_yolk = 70  # °C
room_temp = 20  # °C
fridge_temp = 4  # °C

#mass of smal and large egg
mass_small_egg = 47  # g
mass_large_egg = 67  # g

# Function to calculate cook time
def calculate_cook_time(mass, initial_temp):
    term1 = (mass**(2/3)) * specific_heat_capacity * (density**(1/3))
    term2 = thermal_conductivity * (math.pi**2) * ((4 * math.pi / 3)**(2/3))
    time_seconds = (term1 / term2) * math.log(0.76 * (boiling_water_temp - initial_temp) / (boiling_water_temp - target_temp_yolk))
    time_minutes = time_seconds / 60
    return time_seconds, time_minutes

# Calculations
conditions = [
    ("small egg from fridge", mass_small_egg, fridge_temp),
    ("large egg from fridge", mass_large_egg, fridge_temp),
    ("small egg from room temperature", mass_small_egg, room_temp),
    ("large egg from room temperature", mass_large_egg, room_temp),
]

# Print results
for condition, mass, initial_temp in conditions:
    time_seconds, time_minutes = calculate_cook_time(mass, initial_temp)
    print(f"{condition.capitalize()} cook time: {time_seconds:.0f} s = {time_minutes:.1f} min")

#Had to look a lot up for this one. Neither of us really understood how to do it on our own.
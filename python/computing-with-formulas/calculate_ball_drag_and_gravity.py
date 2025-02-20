import math

drag_coefficient = 0.2
air_density = 1.2  # kg/m^3
ball_radius = 0.11  # m
ball_mass = 0.43  # kg
gravitational_acceleration = 9.81  # m/s^2

# Cross-sectional area of the ball
cross_area = math.pi * ball_radius**2  # m^2

# Forces calculated out
def calculate_forces(velocity):
    # Drag force
    drag_force = 0.5 * drag_coefficient * air_density * cross_area * velocity**2  # N
    # Gravitational force
    gravitational_force = ball_mass * gravitational_acceleration  # N
    # Ratio of drag force to gravitational force
    force_ratio = drag_force / gravitational_force
    return drag_force, gravitational_force, force_ratio
#Used AI to figure out how to do this last paragraph for forces calculated

# Velocities for hard and soft kicks
velocities = [30, 10]  # m/s

#results that are hopefully right
for velocity in velocities:
    drag_force, gravitational_force, force_ratio = calculate_forces(velocity)
    print(f"Velocity: {velocity} m/s")
    print(f"Drag Force: {drag_force:.1f} N")
    print(f"Gravitational Force: {gravitational_force:.1f} N")
    print(f"Ratio of Drag Force to Gravitational Force: {force_ratio:.2f}\n")

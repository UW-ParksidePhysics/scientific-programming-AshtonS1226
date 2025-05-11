import vpython as vp

# Ball setup
initial_position1 = vp.vector(-10.0, -5.0, 0.0)  # Bottom of wall
initial_velocity1 = vp.vector(10.0, 5.0, 0.0)

initial_position2 = vp.vector(-10.0, 5.0, 0.0)   # Top of wall
initial_velocity2 = vp.vector(10.0, -5.0, 0.0)

ball_radius = 0.5

ball1 = vp.sphere(pos=initial_position1, radius=ball_radius, color=vp.color.blue, make_trail=True)
ball2 = vp.sphere(pos=initial_position2, radius=ball_radius, color=vp.color.green, make_trail=True)

# Wall setup
wall_center = vp.vector(0.0, 0.0, 0.0)
wall_dimensions = vp.vector(0.25, 10.0, 10.0)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

# Timing setup
animation_time_step = 0.01  # seconds
rate_of_animation = 1 / animation_time_step
time_step = 0.005
stop_time = 2.0

# Ball velocities
velocity1 = initial_velocity1
velocity2 = initial_velocity2

# Collision threshold (ball radius + half wall thickness)
collision_x = wall.pos.x - (wall.size.x / 2 + ball_radius)

# Animation loop
time = 0.0
while time < stop_time:
    vp.rate(rate_of_animation)

    # Bounce logic for ball 1
    if ball1.pos.x >= collision_x and velocity1.x > 0:
        velocity1.x = -velocity1.x

    # Bounce logic for ball 2
    if ball2.pos.x >= collision_x and velocity2.x > 0:
        velocity2.x = -velocity2.x

    # Update ball positions
    ball1.pos += velocity1 * time_step
    ball2.pos += velocity2 * time_step

    time += time_step

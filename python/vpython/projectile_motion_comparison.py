from vpython import *
import numpy as np

# Set up the scene
scene.width = 1200
scene.height = 600
scene.background = color.white
scene.title = "Projectile Motion Comparison: Earth, Mars, Moon"

# Constants
g_earth = 9.8
g_mars = 3.71
g_moon = 1.62

# Common parameters
theta = np.pi / 6  # 30 degrees, change as desired (between 0 and pi/4)
v0 = 20  # initial speed
ball_radius = 0.5

# Components of velocity
def velocity_components(v0, theta):
    vx = v0 * np.cos(theta)
    vz = v0 * np.sin(theta)
    return vector(vx, 0, vz)

# Field positions
x_spacing = 60
earth_pos = vector(0, 0, 0)
mars_pos = vector(x_spacing, 0, 0)
moon_pos = vector(2 * x_spacing, 0, 0)

# Create fields
field_length = 50
field_width = 10

def create_field(pos, color_field):
    return box(pos=pos + vector(field_length/2, -0.1, 0),
               length=field_length, height=0.2, width=field_width, color=color_field)

earth_field = create_field(earth_pos, color.green)
mars_field = create_field(mars_pos, color.red)
moon_field = create_field(moon_pos, color.gray(0.5))

# Create balls
def create_ball(pos, color_ball):
    return sphere(pos=pos, radius=ball_radius, color=color_ball, make_trail=True, retain=200)

ball_earth = create_ball(earth_pos, color.blue)
ball_mars = create_ball(mars_pos, color.magenta)
ball_moon = create_ball(moon_pos, color.white)

# Labels
label(pos=earth_pos + vector(field_length/2, -1, -field_width/2), text="EARTH", height=2, color=color.green, box=False)
label(pos=mars_pos + vector(field_length/2, -1, -field_width/2), text="MARS", height=2, color=color.red, box=False)
label(pos=moon_pos + vector(field_length/2, -1, -field_width/2), text="MOON", height=2, color=color.gray(0.5), box=False)

# Motion function
def simulate(angle):
    ball_earth.pos = earth_pos
    ball_mars.pos = mars_pos
    ball_moon.pos = moon_pos
    ball_earth.clear_trail()
    ball_mars.clear_trail()
    ball_moon.clear_trail()

    v_earth = velocity_components(v0, angle)
    v_mars = velocity_components(v0, angle)
    v_moon = velocity_components(v0, angle)

    t = 0
    dt = 0.01

    while ball_earth.pos.z >= 0 or ball_mars.pos.z >= 0 or ball_moon.pos.z >= 0:
        rate(100)

        if ball_earth.pos.z >= 0:
            v_earth.z -= g_earth * dt
            ball_earth.pos += v_earth * dt

        if ball_mars.pos.z >= 0:
            v_mars.z -= g_mars * dt
            ball_mars.pos += v_mars * dt

        if ball_moon.pos.z >= 0:
            v_moon.z -= g_moon * dt
            ball_moon.pos += v_moon * dt

        t += dt

# First launch
simulate(theta)
# Pause before second launch
sleep(1)
# Second launch with π/2 − θ
simulate(np.pi/2 - theta)

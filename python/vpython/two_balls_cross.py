
import vpython as vp

# Set up the scene
vp.scene.background = vp.color.white
vp.scene.title = "Two Balls Crossing in 3D Space"

# Initial positions and velocities
position1 = vp.vector(-1, 0, 0)
velocity1 = vp.vector(0.5, 0.2, 0.1)
position2 = vp.vector(1, 0, 0)
velocity2 = vp.vector(-0.5, 0.2, -0.1)

# Create two balls with trails made of small spheres
ball1 = vp.sphere(pos=position1, radius=0.1, color=vp.color.red)
ball2 = vp.sphere(pos=position2, radius=0.1, color=vp.color.blue)

# Time setup
time_step = 0.05
stop_time = 10
current_time = 0

# Animation loop
while current_time < stop_time:
    vp.rate(1 / time_step)

    # Update positions
    position1 += velocity1 * time_step
    position2 += velocity2 * time_step
    ball1.pos = position1
    ball2.pos = position2

    # Leave a trail of spheres behind
    vp.sphere(pos=position1, radius=0.02, color=vp.color.red, opacity=0.4)
    vp.sphere(pos=position2, radius=0.02, color=vp.color.blue, opacity=0.4)

    current_time += time_step

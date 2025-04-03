import vpython as vp
import numpy as np

ball_radius = 1

ball_one = vp.sphere(radius=ball_radius)
ball_two = vp.sphere(radius=ball_radius,
                     color=vp.color.blue,
                     pos=vp.vector(2 * ball_radius,
                                   2*ball_radius,0)
                     )


ball_two_velocity = vp.vector(.01, .01, 0)
ball_two_initial_position = ball_two.pos

times = np.linspace(0,1,100)
time_interval = np.diff(times)[0]
time_frequency = int(1 / time_interval)


times = np.linspace(0, 1, 10_000)

for time in times:
    vp.rate(0.25*time_frequency)
    ball_two.pos += ball_two_velocity * time
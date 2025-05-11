from vpython import *
# GlowScript 3.0 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Set up the 3D scene
scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-0.5, -0.3, -1)

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

# Draw coordinate axes
x_axis = cylinder(color=vector(1, 0, 0), pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)
x_lbl = label(pos=vector(11, 0, 0), text="x", color=color.red, opacity=0, height=30, box=0)

y_axis = cylinder(color=color.green, pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.3)
y_lbl = label(pos=vector(0, 11, 0), text="y", color=color.green, opacity=0, height=30, box=0)

z_axis = cylinder(color=color.blue, pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.3)
z_lbl = label(pos=vector(0, 0, 11), text="z", color=color.blue, opacity=0, height=30, box=0)

# Define vector components based on birthdates: e.g., 6 (June), 14 (14th), 3 (March)
a = 6
b = 14
c = 3

# Draw new light-colored arrow vector in the first octant
vector_r = arrow(pos=vector(0, 0, 0), axis=vector(a, b, c), color=vector(0.8, 0.6, 0.4), shaftwidth=0.5)

# Label the vector with its expression
vector_label = label(
    pos=vector(a + 1, b + 1, c + 1),
    text=r"r = 6x̂ + 14ŷ + 3ẑ",
    height=20,
    box=0,
    color=color.black
)

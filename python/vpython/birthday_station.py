from vpython import *
# GlowScript 3.0 VPython

# Trajectory of a ball thrown on a rotating space station with 'artificial gravity'
# as seen from the inertial frame and from a frame rotating with the space station.

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Classic VPython version Reims, France, August 2010
# GlowScript/CoffeeScript version San Francisco October 2011
# GlowScript/VPython version Santa Fe, March 2015
# Based on a suggestion of Igal Galili at a physics education conference in Reims.

# These "global" variables must be established before the mouse handling reoutines which set them:


# GlowScript 3.0 VPython
# Trajectory of a ball thrown on a rotating space station with 'artificial gravity'
# Adapted from original by Bruce Sherwood. Creative Commons 4.0 license.

# --- Global variables ---
gotv = False
v = vector(0, 0, 0)
pause = False
rotation = 0
drag = False

# --- Birthdates and angular velocity ---
alex_birthdate = 14
sam_birthdate = 13

# Rotation period based on birthdate quotient closest to 1
omega = min(alex_birthdate / sam_birthdate, sam_birthdate / alex_birthdate)

# --- Space Station Class ---
class spacestation:
    def __init__(self, whichcanvas):
        self.N = 50  # number of segments in the ring
        self.R = 10  # inner radius
        self.h = 2   # ball release height
        self.canvas = whichcanvas
        whichcanvas.select()

        self.person = cylinder(pos=vector(0, -self.R, 0),
                               axis=vector(0, self.h, 0),
                               size=vector(self.h, 0.2, 0.2))

        thick = 0.5
        dtheta = 2 * pi / self.N
        use_green = True
        boxes = [self.person]

        for i in range(self.N):
            theta = i * dtheta
            b = box(pos=(self.R + thick / 2) * vector(cos(theta), sin(theta), 0),
                    size=vector(thick, 2 * (self.R + thick) * sin(dtheta / 2), thick))
            if use_green:
                b.color = color.green
            else:
                b.color = color.orange
            use_green = not use_green
            b.rotate(angle=theta, axis=vector(0, 0, 1))
            boxes.append(b)

        self.hull = compound(boxes)

        self.ball = sphere(pos=self.person.pos + self.person.axis,
                           color=color.magenta, size=vector(0.4, 0.4, 0.4))
        self.trail = attach_trail(self.ball, radius=0.1 * self.ball.size.x, pps=10, retain=500)
        self.reset()

    def reset(self):
        global rotation
        self.hull.rotate(angle=-rotation, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
        self.ball.pos = self.person.pos + self.person.axis
        self.trail.clear()
        rotation = 0

# --- Mouse input handler ---
def bind_mouse(station, vector1, vector2):
    global pause
    if pause:
        return
    s = station.canvas

    def down():
        global drag, gotv, v

        def set_v():
            vector1.axis = s.mouse.pos - vector1.pos
            vector2.axis = vector1.axis
            if station is station1:
                vector2.axis.x -= scalefactor * v0
            else:
                vector2.axis.x += scalefactor * v0
                vector2.size.x = mag(vector2.axis)

        set_v()
        drag = True

        def move():
            global drag, pause
            if pause:
                return
            if drag:
                set_v()

        def up():
            global drag, gotv, v, pause
            if pause:
                pause = False
                return
            drag = False
            if mag(vector1.axis) <= station.ball.size.y / 2:
                vector1.axis = vector(0, 0, 0)
            elif mag(vector2.axis) <= station.ball.size.y / 2:
                vector2.axis = vector(0, 0, 0)
            if station is station1:
                v = vector1.axis / scalefactor
            else:
                v = vector2.axis / scalefactor
            gotv = True

        s.bind("mousemove", move)
        s.bind("mouseup", up)

    s.bind("mousedown", down)

# --- Scene setup ---
scene1 = canvas(width=430, height=400, align='left', userspin=False, userzoom=False)
scene2 = canvas(width=430, height=400, align='left', userspin=False, userzoom=False)

scene1.title = """ROTATING SPACE STATION
Inertial frame on the left, rotating frame on the right."""

station1 = spacestation(scene1)
station2 = spacestation(scene2)

scene1.autoscale = scene2.autoscale = False
deltat = 0.001 * 2 * pi / omega
v0 = omega * (station1.R - station1.h)
scalefactor = 5 / (omega * station1.R)

v1 = arrow(canvas=scene1, pos=station1.ball.pos, color=color.green,
           axis=vector(0, 0, 0), shaftwidth=0.4, visible=False)

v2 = arrow(canvas=scene2, pos=station2.ball.pos, color=color.green,
           axis=vector(0, 0, 0), shaftwidth=0.4, visible=False)

instruct1 = label(canvas=scene1, pos=vector(0, station1.R / 2, 0),
                  text="Drag initial velocity in the inertial frame",
                  visible=False)

instruct2 = label(canvas=scene2, pos=vector(0, station2.R / 2, 0),
                  text="Or drag initial velocity relative to rotating space station",
                  visible=False)

click1 = label(canvas=scene1, pos=vector(0.8 * station1.R, -1 * station1.R, 0),
               text="Click to\nstart over", visible=False)

click2 = label(canvas=scene2, pos=vector(0.8 * station2.R, -1 * station2.R, 0),
               text="Click to\nstart over", visible=False)

bind_mouse(station1, v1, v2)
bind_mouse(station2, v2, v1)

# --- Main loop ---
while True:
    station1.reset()
    station2.reset()
    v1.axis = vector(0, 0, 0)
    v2.axis = vector(0, 0, 0)
    v1.visible = v2.visible = True
    instruct1.visible = instruct2.visible = True

    while True:
        rate(50)
        if gotv:
            break

    v1.visible = v2.visible = False
    instruct1.visible = instruct2.visible = False
    r = vector(station1.ball.pos)
    t = 0

    while True:
        rate(0.5 / deltat)
        rotation += omega * deltat

        station1.ball.rotate(angle=omega * deltat, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
        station1.hull.rotate(angle=omega * deltat, axis=vector(0, 0, 1), origin=vector(0, 0, 0))

        r = r + v * deltat
        station1.ball.pos = r
        newr = vector(r)
        station2.ball.pos = newr.rotate(angle=-omega * t, axis=vector(0, 0, 1))

        if mag(station1.ball.pos) >= station1.R:
            direction = norm(station1.ball.pos)
            station1.ball.pos = station1.R * direction
            direction = norm(station2.ball.pos)
            station2.ball.pos = station2.R * direction
            break

        t += deltat

    click1.visible = click2.visible = True
    pause = True
    while True:
        rate(50)
        if not pause:
            break
    gotv = False
    click1.visible = click2.visible = False

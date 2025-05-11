import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def wave_packet(x, t, alpha, f, k, omega):
    """Compute wave packet function for given parameters."""
    return np.exp(-((alpha * x - f * t) ** 2)) * np.sin(k * x - omega * t)

# Parameters
alpha = 1
f = 3
k = 3 * np.pi
omega = 3 * np.pi

x = np.linspace(-6, 6, 1001)           # 1001 points in space
t_values = np.linspace(-1, 1, 61)      # 61 time steps

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(-6, 6)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel('x')
ax.set_ylabel('f(x, t)')
ax.set_title('Wave Packet Animation')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = t_values[frame]
    y = wave_packet(x, t, alpha, f, k, omega)
    line.set_data(x, y)
    ax.set_title(f'Wave Packet at t = {t:.2f}')
    return line,

ani = animation.FuncAnimation(
    fig, update, frames=len(t_values), init_func=init, blit=True, interval=1000/6
)

# Save animation as GIF
ani.save('wavepacket.gif', writer='pillow', fps=6)

# Show the animation
plt.show()
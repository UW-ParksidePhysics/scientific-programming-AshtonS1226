#initial velocity
v0 = 10.0

#gravitational acceleration
g = 9.81

#number of steps
n=8

# maximum time
t_max = 2 *v0 / g

# time interval
dt = t_max / n

times = []
positions = []

for i in range(n+1):
    t = i * dt
    y = v0 * t - 0.5 * g * t**2
    times.append(t)
    positions.append(y)

# table header
print("Vertical motion under gravity (Earth, g = 9.81 m/s^2)")
print("-" * 36)
print(f"{'t (s)':>8} {'y (m)':>10}")
print(f"{'-'*8} {'-'*10}")

#lists in parallel
for t, y in zip(times, positions):
    print(f"{t:8.2f} {y:10.3f}")


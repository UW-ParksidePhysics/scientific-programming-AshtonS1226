# constants
v0 = 5 #m/s
g = 9.81 #m/s^2
n = 11
dt = 0.1

times = []
positions = []

for i in range(n):
    t = i * dt
    y = v0 * t - 0.5 * g * t**2
    times.append(t)
    positions.append(y)

# Nested list
times_positions = [times, positions]

#header for table
print(f"{'t (s)':>8} {'y (m)':>8}")
for i in range(len(times_positions[0])):
    t = times_positions[0][i]
    y = times_positions[1][i]
    print(f"{t:8.2f} {y:8.2f}")

# Nested list of rows
time_positions = []
for i in range(n):
    row = [times[i], positions[i]]
    time_positions.append(row)

#row-wise table
print("\nFrom time_positions (rows):")
for row in time_positions:
    t, y = row
    print(f"{t:8.2f} {y:8.2f}")

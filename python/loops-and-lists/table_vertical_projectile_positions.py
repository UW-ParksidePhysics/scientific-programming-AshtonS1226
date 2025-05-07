# initial velocity
v0 = 10.0 # m/s

#gravitational acceleration
g1 = 9.8 #m/s^2  Earth
g2 = 12.94  #Cc (exoplanet)

n = 8

#time intervals
t_max1 = 2 * v0 / g1
t_max2 = 2 * v0 / g2

dt1 = t_max1 / n
dt2 = t_max2 / n

# table header
print("For initial velocity of 10.00 m/s:")
print("-" * 72)
print("Gliese 667 Cb (g = 14.12 m/s^2) Cc (g = 12.94 m/s^2)")
print("-" * 72)
print(f"{'t (s)':>6} {'y (m)':>7}   {'t (s)':>6} {'y (m)':>7}")
print(f"{'-'*6} {'-'*7} {'-'*6} {'-'*7}")
print("using a for loop")

for i in range(n + 1):
    t1 = i * dt1
    y1 = v0 * t1 - 0.5 * g1 * t1**2

    t2 = i * dt2
    y2 = v0 * t2 - 0.5 * g2 * t2**2

    print(f"{t1:6.3f} {y1:7.3f} {t2:6.3f} {y2:7.3f}")

print("\nusing a while loop:")


i = 0
t1 = 0.0
t2 = 0.0
while t1 <= t_max1 + 0.0001 or t2 <= t_max2 + 0.0001:
    if t1 <= t_max1 + 0.0001:
        y1 = v0 * t1 - 0.5 * g1 * t1**2
        print(f"{t1:6.3f} {y1:7.3f}", end="   ")
        t1 += dt1
    else:
        print(" " * 15, end="   ")

    if t2 <= t_max2 + 0.0001:
        y2 = v0 * t2 - 0.5 * g2 * t2**2
        print(f"{t2:6.3f} {y2:7.3f}")
        t2 += dt2
    else:
        print()
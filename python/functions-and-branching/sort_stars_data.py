nearby_star_data = [
    ('Alpha Centauri A',    4.3,  0.26,      1.56),
    ('Alpha Centauri B',    4.3,  0.077,     0.45),
    ('Alpha Centauri C',    4.2,  0.00001,   0.00006),
    ("Barnard's Star",      6.0,  0.00004,   0.0005),
    ('Wolf 359',            7.7,  0.000001,  0.00002),
    ('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
    ('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
    ('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
    ('Sirius A',            8.6,  1.00,      23.6),
    ('Sirius B',            8.6,  0.001,     0.003),
    ('Ross 154',            9.4,  0.00002,   0.0005),
]

def sort_by_distance(star):
    return star[1]

def sort_by_brightness(star):
    return star[2]

def sort_by_luminosity(star):
    return star[3]

def print_table(header1, header2, data, key_index):
    print(f"\n{header1:<25} {header2}")
    print("-" * 40)
    for star in data:
        print(f"{star[0]:<25} {star[key_index]:.6f}")


sorted_by_distance = sorted(nearby_star_data, key=sort_by_distance)
print_table("Star Name", "Distance (1y)", sorted_by_distance, 1)

sorted_by_brightness = sorted(nearby_star_data, key=sort_by_brightness)
print_table("Star Name", "Apparent Brightness", sorted_by_brightness, 2)

sorted_by_luminosity = sorted(nearby_star_data, key=sort_by_luminosity)
print_table("Star Name", "Luminosity", sorted_by_luminosity, 3)




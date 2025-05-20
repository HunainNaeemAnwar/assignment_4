earth_weight = float(input("Enter a weight on Earth: "))

planet = input("Enter a planet : ")

gravity_map = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

planet_gravity = gravity_map[planet]
planet_weight = earth_weight * planet_gravity

print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")

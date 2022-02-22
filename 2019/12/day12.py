from point import Point
from moon import Moon

moons = [
    Moon(Point(-5, 6, -11)),
    Moon(Point(-8, -4, -2)),
    Moon(Point(1, 16, 4)),
    Moon(Point(11, 11, -4))
]

for i in range(0, 1000):
    for this_moon in moons:
        for other_moon in moons:
            if (this_moon == other_moon):
                continue
            
            this_moon.apply_gravity(other_moon)
    
    for moon in moons:
        moon.apply_velocity()

energy = 0

for moon in moons:
    energy += moon.get_energy()

print(energy)
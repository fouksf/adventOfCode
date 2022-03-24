from point import Point
from moon import Moon

moons = [
    Moon(Point(5, -1, 5)),
    Moon(Point(0, -14, 2)),
    Moon(Point(16, 4, 0)),
    Moon(Point(18, 1, 16))
]
# First example
    # Moon(Point(-1, 0, 2)),
    # Moon(Point(2, -10, -7)),
    # Moon(Point(4, -8, 8)),
    # Moon(Point(3, 5, -1))

# #second example
#     Moon(Point(-8, -10, 0)),
#     Moon(Point(5, 5, 10)),
#     Moon(Point(2, -7, 3)),
#     Moon(Point(9, -8, -3))

# fo's input
    # Moon(Point(5, -1, 5)),
    # Moon(Point(0, -14, 2)),
    # Moon(Point(16, 4, 0)),
    # Moon(Point(18, 1, 16))
# Nick's input
    # Moon(Point(-5, 6, -11)),
    # Moon(Point(-8, -4, -2)),
    # Moon(Point(1, 16, 4)),
    # Moon(Point(11, 11, -4))


## Part One
# for i in range(0, 1000):
#     for this_moon in moons:
#         for other_moon in moons:
#             if (this_moon == other_moon):
#                 continue
            
#             this_moon.apply_gravity(other_moon)
    
#     for moon in moons:
#         moon.apply_velocity()

# energy = 0

# for moon in moons:
#     energy += moon.get_energy()

# print(energy)


## Part two

from moonSystem import MoonSystem
moon_system = MoonSystem(moons)
print(moon_system.find_cycle())

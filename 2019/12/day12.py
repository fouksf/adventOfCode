from point import Point
from moon import Moon

moons = [
    Moon(Point(-1, 0, 2)),
    Moon(Point(2, -10, -7)),
    Moon(Point(4, -8, 8)),
    Moon(Point(3, 5, -1))
]
# First example
    # Moon(Point(-1, 0, 2)),
    # Moon(Point(2, -10, -7)),
    # Moon(Point(4, -8, 8)),
    # Moon(Point(3, 5, -1))

# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>

# fo's input
    # Moon(Point(5, -1, 5)),
    # Moon(Point(0, -14, 2)),
    # Moon(Point(16, 4, 0)),
    # Moon(Point(18, 1, 16))



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

moon_system = MoonSystem(moons)
print(moon_system.find_cycle())

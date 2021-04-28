def parseInput(input):
    orbits = input.split("\n")

    parsed_input = []

    for orbit in orbits:
        split = orbit.split(")")
        planet = split[0]
        satelite = split[1]

        parsed_input.append((planet, satelite))
    
    return parsed_input

class Satellite:
    def __init__(self, name):
        self.name = name
        self.satellites = []
    
    def __str__(self):
        return f'{self.name}: {self.satellites}'



def create_orbit_structure():
    orbit_structure = {}

    input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
    orbits = parseInput(input)

    for orbit in orbits:
        (center_of_mass, satellite) = orbit

        if (center_of_mass in orbit_structure):
            orbit_structure[center_of_mass].satellites.append(satellite)
        else:
            orbit_structure[center_of_mass] = Satellite(center_of_mass)
            orbit_structure[center_of_mass].satellites.append(satellite)
        
        if (satellite not in orbit_structure):
            orbit_structure[satellite] = Satellite(satellite)

    return orbit_structure

def calculate_hash():
    orbit_structure = create_orbit_structure()

    for thing in orbit_structure:
        print(orbit_structure[thing])
    # start = orbit_structure['COM']

    total_direct_orbits = 0

    for object in orbit_structure:
        direct_orbits = len(orbit_structure[object].satellites)
        total_direct_orbits += direct_orbits
    
    return total_direct_orbits
    
# find all of the things that are orbiting the current thing
print(calculate_hash())
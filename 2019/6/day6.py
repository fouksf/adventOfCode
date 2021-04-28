input = open("2019/6/input.txt", "r").read()

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
    total = 0
    orbit_structure = create_orbit_structure()

    def count_links(orbiter):
        links = len(orbiter.satellites)

        for satellite in orbiter.satellites:
            links += count_links(orbit_structure[satellite])

        return links
    
    for orbit in orbit_structure:
        total += count_links(orbit_structure[orbit])

    return total

# find all of the things that are orbiting the current thing
print(calculate_hash())
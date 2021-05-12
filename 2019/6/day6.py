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
        self.com = ''
        self.satellites = []

    def __str__(self):
        return f'{self.name}: {self.satellites}'
    
    def setCom(self, com):
        self.com = com



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
        orbit_structure[satellite].setCom(center_of_mass)

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

def findPathToCom(orbit_structure, satellite_name):
    current_satellite = satellite_name
    path = []
    while current_satellite != "COM":
        path.append(current_satellite)
        current_satellite = orbit_structure[current_satellite].com
    # path.appent("COM")
    return path

def findShortestDistance(orbit_structure, starting_point, finish_point):
    first_path = findPathToCom(orbit_structure, starting_point)
    second_path = findPathToCom(orbit_structure, finish_point)
    for satellite in first_path:
        if satellite in second_path:
            return first_path.index(satellite) + second_path.index(satellite) - 2

# find all of the things that are orbiting the current thing
print(calculate_hash())

print(findShortestDistance(create_orbit_structure(), "YOU", "SAN"))
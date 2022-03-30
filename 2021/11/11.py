input = open("2021/11/input.txt", "r").read().split("\n")

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.has_flashed = False
    def __repr__(self):
        return f'({self.energy}, {self.has_flashed})'

octopi = list(map(lambda l: list(map(lambda o: Octopus(int(o)), list(l))), input))

def illuminate_surrounding(octopi, i, j):
    octopi[i][j].has_flashed = True
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if(i + dx < 0 or i + dx >= len(octopi) or j + dy < 0 or j + dy >= len(octopi[0])):
                continue
            octopi[i + dx][j + dy].energy += 1

def do_flashes(octopi):
    for i in range(0, len(octopi)):
        for j in range(0, len(octopi[0])):
            if octopi[i][j].energy > 9 and octopi[i][j].has_flashed == False:
                illuminate_surrounding(octopi, i, j)

def has_unflashed(octopi):
    return True in map(lambda l: True in map(lambda o: o.energy > 9 and o.has_flashed == False, l), octopi)

def step(octopi):
    for octopus in [o for line in octopi for o in line]:
        octopus.energy += 1
    while has_unflashed(octopi):
        do_flashes(octopi)
    flashes = sum(map(lambda l: sum(map(lambda o: 1 if o.has_flashed else 0, l)), octopi))
    for octopus in [o for line in octopi for o in line]:
        if octopus.has_flashed:
            octopus.has_flashed = False
            octopus.energy = 0
        
    return flashes

flashes = 0
i = 1
while True:
    flashes = step(octopi)
    if flashes == 100:
        print(i)
        break
    i += 1


    
    


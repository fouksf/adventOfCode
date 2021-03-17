numbersFile = open("2019/3/input.txt", "r")

instructions = numbersFile.read().split("\n")
lineOne = instructions[0].split(",")
lineTwo = instructions[1].split(",")

def makeSet(instructions):
    visited = set()
    x = 0
    y = 0
    steps = 0
    steps_hash = {}

    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        for _ in range(magnitude):
            steps = steps + 1
            if direction == 'R':
                x += 1
            if direction == 'L':
                x -= 1
            if direction == 'U':
                y += 1
            if direction == 'D':
                y -= 1
            
            coords = (x, y)
            steps_hash[coords] = steps
            visited.add(coords)

    return (visited, steps_hash)

firstSet, firstHash = makeSet(lineOne)
secondSet, secondHash = makeSet(lineTwo)

intersection = firstSet.intersection(secondSet)

# PART 2
def calculate_steps(tuple):
    distance_one = firstHash[tuple]
    distance_two = secondHash[tuple]

    return distance_one + distance_two

total_steps = list(map(calculate_steps, intersection))
total_steps.sort()

print(total_steps[0])

# PART 1
def calculateDistance(tuple):
    x, y = tuple

    return abs(x) + abs(y)

distances = list(map(calculateDistance, intersection))
distances.sort()
print(distances[0])
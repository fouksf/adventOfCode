numbersFile = open("2019/3/input.txt", "r")

instructions = numbersFile.read().split("\n")
lineOne = instructions[0].split(",")
lineTwo = instructions[1].split(",")

def makeSet(instructions):
    visited = set()
    x = 0
    y = 0

    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        for _ in range(magnitude):
            if direction == 'R':
                x += 1
            if direction == 'L':
                x -= 1
            if direction == 'U':
                y += 1
            if direction == 'D':
                y -= 1
            
            coords = (x, y)
            visited.add(coords)

    return visited

firstSet = makeSet(lineOne)
secondSet = makeSet(lineTwo)

intersection = firstSet.intersection(secondSet)

def calculateDistance(tuple):
    x, y = tuple

    return abs(x) + abs(y)

distances = list(map(calculateDistance, intersection))
distances.sort()

print(distances)

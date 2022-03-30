import copy

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

def parseInput():
    instructionsFile = open("solutions/day12/instructions.txt", "r")
    instructions = instructionsFile.read().split("\n")
    instructionsFile.close()
    return instructions

def turn(currentDirection, turnTo, degrees):
    directionIndex = DIRECTIONS.index(currentDirection)
    if turnTo == RIGHT:
        step = degrees // 90
    elif turnTo == LEFT:
        step = -1 * (degrees // 90)
        step += len(DIRECTIONS)
    return DIRECTIONS[abs(directionIndex + step) % len(DIRECTIONS)]

def moveWaypoint(waypoint, direction, value):
    if direction == NORTH:
        waypoint[1] += value
    elif direction == SOUTH:
        waypoint[1] -= value
    elif direction == EAST:
        waypoint[0] += value
    elif direction[0] == WEST:
        waypoint[0] -= value
    else: 
        raise Exception("wtf")

def rotateWaypoint(waypoint, direction, value):
    steps = value // 90
    if direction == LEFT:
        steps = 4 - steps
    if steps % 2 == 0:
        newWaypoint = [-1 * waypoint[0], -1 * waypoint[1]]
    else:
        newWaypoint = [waypoint[1], waypoint[0]]
        if steps == 1:
            newWaypoint[1] *= -1 
        else: 
            newWaypoint[0] *= -1
    return newWaypoint
    
def moveToWaypoint(currentPosition, waypoint, value):
    return [currentPosition[0] + value * waypoint[0], currentPosition[1] + value * waypoint[1]]

def getManhattanSum(instructions):
    position = [0, 0]
    waypoint = [10, 1]
    movement = dict(zip(DIRECTIONS, [0] * len(DIRECTIONS)))
    for instruction in instructions:
        print(f'Position: {position}')
        print(f'Waypoint: {waypoint}')
        print(instruction)
        direction = instruction[0]
        value = int(instruction[1:])
        if direction in DIRECTIONS:
            moveWaypoint(waypoint, direction, value)
        elif direction == FORWARD:
            position = moveToWaypoint(position, waypoint, value)
        else:
            waypoint = rotateWaypoint(waypoint, direction, value)
    return abs(position[0]) + abs(position[1])


instructions = parseInput()
print(getManhattanSum(instructions))
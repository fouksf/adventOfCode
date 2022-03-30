
EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

import copy 

def parseInput():
    seatsFile = open("solutions/day11/seats.txt", "r")
    seats = list(map(list, seatsFile.read().split("\n")))
    seatsFile.close()
    return seats

def findOccupiedNeighbours(seats, i, j):
    count = 0
    for k in range(i - 1, i + 2):
        if k >= 0 and k < len(seats):
            for l in range(j - 1, j + 2):
                if l >= 0 and l < len(seats[k]) and (k != i or l != j):
                    if seats[k][l] == OCCUPIED:
                        count += 1
    return count

def updateSeats(seats):
    newSeats = copy.deepcopy(seats)
    changed = 0
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            occupiedNeighbours = findOccupiedNeighbours(seats, i, j)
            if seats[i][j] == EMPTY and occupiedNeighbours == 0:
                newSeats[i][j] = OCCUPIED
                changed += 1
            elif seats[i][j] == OCCUPIED and occupiedNeighbours >= 4:
                newSeats[i][j] = EMPTY
                changed +=1 
    return (newSeats, changed)

def findOrder(seats):
    seatsChanged = 1
    currentSeats = copy.deepcopy(seats)
    while seatsChanged != 0:
        (currentSeats, seatsChanged) = updateSeats(currentSeats)
    return ''.join([seat for row in currentSeats for seat in row]).count(OCCUPIED)

seats = parseInput()
print(findOrder(seats))
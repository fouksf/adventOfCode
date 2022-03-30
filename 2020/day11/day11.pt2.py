
EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

import copy
import itertools 

def parseInput():
    seatsFile = open("solutions/day11/seats.txt", "r")
    seats = list(map(list, seatsFile.read().split("\n")))
    seatsFile.close()
    return seats

def findOccupiedNeighbours(seats, i, j):
    count = 0
    for step in itertools.product(range(-1, 2), range(-1, 2)):
        if step[0] == 0 and step[1] == 0:
            continue
        k = i + step[0]
        l = j + step[1]
        while k >= 0 and k < len(seats) and l >= 0 and l < len(seats[step[0]]):
            if seats[k][l] == OCCUPIED:
                count += 1
                break
            if seats[k][l] == EMPTY:
                break
            k += step[0]
            l += step[1]
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
            elif seats[i][j] == OCCUPIED and occupiedNeighbours >= 5:
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
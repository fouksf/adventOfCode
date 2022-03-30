import math
seatsFile = open("solutions/day5/seats.txt", "r")
seats = seatsFile.read().split("\n")
seatsFile.close()

FRONT = "F"
BACK = "B"
LEFT = "L"
RIGHT = "R"


def getSeatNumber(map, max, lower, upper):
    min = 0
    for letter in map:
        if letter == lower:
            max = max - math.ceil((max - min) / 2)
        elif letter == upper:
            min = min + math.ceil((max - min) / 2)
        else:
            return -2
    if min == max:
        return min
    return -1


def getSeatId(seat):
    return getSeatNumber(seat[0:7], 127, FRONT, BACK) * 8 + getSeatNumber(seat[-3:], 7, LEFT, RIGHT)

maxId = 0
for seat in seats:
    maxId = max(maxId, getSeatId(seat))

print("*" * 10, "First part", "*" * 10)
print(maxId)

print("*" * 10, "Second part", "*" * 10)

ids = []
for seat in seats:
    ids.append(getSeatId(seat))

ids.sort()
for i in range(1, len(ids)):
    if(ids[i] - ids[i - 1] != 1):
        print(ids[i] - 1)





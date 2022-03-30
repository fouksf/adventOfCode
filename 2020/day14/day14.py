def parseInput():
    inputFile = open("solutions/day14/masks.txt", "r")
    lines = inputFile.read().split("\n")
    inputFile.close()
    arrivalTime = int(lines[0])
    buses = list(map(int, filter(lambda b: b != "x", lines[1].split(","))))
    return (arrivalTime, buses)

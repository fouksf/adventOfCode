def parseInput():
    busesFile = open("solutions/day13/buses.txt", "r")
    lines = busesFile.read().split("\n")
    busesFile.close()
    arrivalTime = int(lines[0])
    buses = list(map(int, filter(lambda b: b != "x", lines[1].split(","))))
    return (arrivalTime, buses)

def findFirstBus(arrivalTime, buses):
    waitTimes = {}
    firstBus = buses[0]
    for bus in buses:
        waitTime = (bus - arrivalTime % bus) % bus
        waitTimes[bus] = waitTime
        if waitTime < waitTimes[firstBus]:
            firstBus = bus
    return firstBus * waitTimes[firstBus]
[arrivalTime, buses] = parseInput()
print(findFirstBus(arrivalTime, buses))
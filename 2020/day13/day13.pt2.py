def parseInput():
    busesFile = open("solutions/day13/buses.txt", "r")
    buses = busesFile.read().split("\n")[1].split(",")
    busesFile.close()
    departures = []
    for i, bus in enumerate(buses):
        if bus != "x":
            departures.append((int(bus), (int(bus) - i) % int(bus)))
    departures.sort(key = lambda x: x[1], reverse = True)
    return departures

def checkTime(buses, t):
    for bus in buses:
            if t % bus[0] != bus[1]:
                return False
    return True

def findFitstT(buses):
    t = 100000000000000
    found = False
    while not found:
        if checkTime(buses, t):
            found = True
        else:
            t += buses[0][0]
    return t

departures = parseInput()
print(departures)
print(findFitstT(departures))
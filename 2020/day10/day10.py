
def parseInput():
    adaptorsFile = open("solutions/day10/adapters.txt", "r")
    adapters = list(map(int, adaptorsFile.read().split("\n")))
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    adaptorsFile.close()
    return adapters

def findWaysToConnectToNext(currentAdapter, nextAdapters):
    count = 0
    for i in range(0, len(nextAdapters)):
        if nextAdapters[i] - currentAdapter <= 3:
            count += 1
    return count

def findAllWaysToConnect(adapters, checked):
    firstLast = (adapters[0], adapters[-1])
    if firstLast in checked:
        return checked[firstLast]
    count = 0
    if len(adapters) == 3:
        if(adapters[2] - adapters[0] <= 3):
            checked[firstLast] = 2
            return 2
        return 1
    if len(adapters) == 2:
        checked[firstLast] = 1
        return 1
    if len(adapters) == 1:
        checked[firstLast] = 0
        return 0
    for j in range(1,4):
        if j < len(adapters):
            if adapters[j] - adapters[0] <= 3:
                a = findAllWaysToConnect(adapters[j:], checked)
                count += a
    checked[firstLast] = count
    return count

def findJoltDifferences(adapters):
    differences = [0] * 3
    for i in range(1, len(adapters)):
        difference = adapters[i] - adapters[i - 1]
        differences[difference - 1] += 1
    return differences



adapters = parseInput()
differences = findJoltDifferences(adapters)
print(findAllWaysToConnect(adapters, {}))
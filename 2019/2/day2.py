numbersFile = open("2019/2/input.txt", "r")
numbers = list(map(int, numbersFile.read().split(",")))
SUM = 1
MULTIPLY = 2
HALT = 99

DESIRED_OUTPUT = 19690720

def runIntCode(operations):
    for i in range(0, len(operations), 4):
        if operations[i] == HALT:
            break
        firstIndex = operations[i + 1]
        secondIndex = operations[i + 2]
        sumIndex = operations[i + 3]
        if operations[i] == SUM:
            operations[sumIndex] = operations[firstIndex] + operations[secondIndex]
        elif operations[i] == MULTIPLY:
            operations[sumIndex] = operations[firstIndex] * operations[secondIndex]
    return operations[0]

def findNounAndVerb(operations):
    output = operations[0]

    for i in range(0, 100):
        for j in range(0, 100):
            currentOperations = operations.copy()
            currentOperations[1] = i
            currentOperations[2] = j
            if runIntCode(currentOperations) == DESIRED_OUTPUT:
               return 100 * i + j


print(findNounAndVerb(numbers))
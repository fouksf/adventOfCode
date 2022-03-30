import math

PREAMBLE_LEN = 25

def parseInput():
    numbersFile = open("solutions/day9/numbers.txt", "r")
    numbers = list(map(int, numbersFile.read().split("\n")))
    numbersFile.close()
    return numbers

def checkIfTwoSumUpTo(number, list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == number:
                return True
    return False


def findFirstIncorrect(numbers, preambleLen):
    min = 0
    while min + preambleLen < len(numbers):
        if not checkIfTwoSumUpTo(numbers[min + preambleLen], numbers[min : min + preambleLen]):
            return numbers[min + preambleLen]
        min += 1

def sumMinMax(numbers):
    return min(numbers) + max(numbers)



def findWeakness(numbers, sum):
    for i in range(0, len(numbers)):
        currentSum = 0
        for j in range(i, len(numbers)):
            currentSum += numbers[j]
            if currentSum == sum:
                return sumMinMax(numbers[i:j + 1])
    raise Exception("Didn't find anything")


numbers = parseInput()
print(findWeakness(numbers, findFirstIncorrect(numbers, PREAMBLE_LEN)))
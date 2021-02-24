import functools
import math

numbersFile = open("2019/1/input.txt", "r")
numbers = list(map(int, numbersFile.read().split("\n")))


# take its mass, divide by three, round down, and subtract 2.
def calculateFuel(mass):
    return math.floor(mass / 3) - 2

def calculateFuelForFuel(mass):
    print(mass)
    allFuel = 0
    currentFuel = calculateFuel(mass)
    while currentFuel > 0:
        allFuel += currentFuel
        currentFuel = calculateFuel(currentFuel)
    print(allFuel)
    return allFuel

print(functools.reduce(lambda a,b : a + calculateFuelForFuel(b), numbers, 0))


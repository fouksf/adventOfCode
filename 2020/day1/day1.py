numbersFile = open("numbers.txt", "r")
numbers = list(map(int, numbersFile.read().split("\n")))
numbers.sort()

desiredSum = 2020

for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == desiredSum:
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                break
            elif a + b + c > desiredSum:
                pass

numbersFile.close

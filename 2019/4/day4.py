input = "240298-784956"

start = 240298
end = 784956


# 6 digit number
# value in above range
# two adjacent digits are the same
# digits never decrease

def findNumber():
    count = 0
    for i in range(start + 1, end):
        if numberCompliesPt2(i):
            count += 1
    
    return count

def numberComplies(number):
    hasRepeatingDigit = False
    hasIncreasingDigits = True

    string = str(number)
    
    for i in range(len(string) - 1):
        digitOne = string[i]
        digitTwo = string[i + 1]

        if digitTwo == digitOne:
            hasRepeatingDigit = True

        if digitTwo < digitOne:
            hasIncreasingDigits = False

    return hasRepeatingDigit and hasIncreasingDigits


def numberCompliesPt2(number):
    hasGroupOfTwo = False
    hasIncreasingDigits = True
    groupCounter = 1

    string = str(number)
    
    for i in range(len(string) - 1):
        digitOne = string[i]
        digitTwo = string[i + 1]

        if digitTwo == digitOne:
            groupCounter += 1
        else:
            if groupCounter == 2:
                hasGroupOfTwo = True
            groupCounter = 1

        if digitTwo < digitOne:
            hasIncreasingDigits = False
    if groupCounter == 2:
        hasGroupOfTwo = True

    return hasGroupOfTwo and hasIncreasingDigits


number = findNumber()
print(number)

# print(numberCompliesPt2(112233))
# print(numberCompliesPt2(123444))
# print(numberCompliesPt2(111122))
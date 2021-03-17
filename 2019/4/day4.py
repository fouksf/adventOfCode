input = "382345-843167"

start = 382345
end = 843167


# 6 digit number
# value in above range
# two adjacent digits are the same
# digits never decrease

def findNumber():
    count = 0
    for i in range(start + 1, end):
        if numberComplies(i):
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

number = findNumber()
print(number)

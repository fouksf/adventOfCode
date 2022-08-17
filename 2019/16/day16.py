import math

inpt = list(map(int, list(open("2019/16/input.txt", "r").read().strip())))

def desired_index(i, pos):
    pattern = [0, 1, 0, -1]
    index = math.floor((i + 1)/pos) % len(pattern)
    return pattern[index]


def calculate(inp):
    out = []

    for pos in range(1, len(inp)+1):
        sum = 0

        for i in range(0, len(inp)):
            sum += desired_index(i, pos) * inp[i]

        sum = abs(sum)
        out.append(sum % 10)

    return out


for i in range(0, 100):
    inpt = calculate(inpt)

print(inpt)

import itertools
from collections import Counter

class Foo:
    def __init__(self, depth, basin):
        self.depth = depth
        self.basin = basin


def is_low_point(i, j, input):
    if((i - 1 >= 0 and input[i - 1][j] <= input[i][j]) or
        (i + 1 < len(input) and input[i + 1][j] <= input[i][j]) or
        (j - 1 >= 0 and input[i][j -1] <= input[i][j]) or
        (j + 1 < len(input[0]) and input[i][j + 1] <= input[i][j])):
        return False
    return True

# sum = 0
# for i in range(0, len(input)):
#     for j in range(0, len(input[0])):
#         if is_low_point(i, j, input):
#             sum += input[i][j] + 1

# print(sum)

## part 2

class Foo:
    def __init__(self, depth, basin):
        self.depth = depth
        self.basin = basin

    def __repr__(self):
        return f'({self.depth}, {self.basin})'

input = list(map(lambda l: list(map(lambda x: Foo(int(x), None), list(l))), open("2021/9/input.txt", "r").read().split("\n")))

def mark_basin(input, i, j, basin):
    if i < 0 or j < 0 or i >= len(input) or j >= len(input[0]) or input[i][j].depth == 9 or input[i][j].basin != None:
        return
    input[i][j].basin = basin
    mark_basin(input, i - 1, j, basin)
    mark_basin(input, i + 1, j, basin)
    mark_basin(input, i, j - 1, basin)
    mark_basin(input, i, j + 1, basin)

basin = 1
for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        mark_basin(input, i, j, basin)
        basin += 1

basins = list(filter(lambda b: b != None, list(map(lambda x: x.basin, [item for sublist in input for item in sublist]))))

sett = set(basins)
counts = []
for basin in sett:
    counts.append(basins.count(basin))

counts = sorted(counts)
counts.reverse()
 

print(counts[0] * counts[1] * counts[2])


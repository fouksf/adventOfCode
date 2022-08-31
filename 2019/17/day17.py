from intcode import Computer

inp = list(map(int, open("2019/17/input.txt", "r").read().strip().split(",")))
intcode = Computer(inp)

SCAFFOLDING = "#"

grid = []
row = []
for i in range(0,2653):
    num = intcode.run_int_code([])

    if num == 10:
        grid.append(row)
        row = []
    else:
        row.append(chr(num))

for line in grid:
    print(''.join(line))

def isIntersection(i, j, grid):
    return grid[i][j] == SCAFFOLDING and grid[i - 1][j] == SCAFFOLDING and grid[i + 1][j] == SCAFFOLDING and grid[i][j + 1] == SCAFFOLDING and grid[i][j - 1] == SCAFFOLDING

def calculateAlignmentParameter(i, j, grid):
    if isIntersection(i, j, grid):
        return i * j
    else:
        return 0

sum = 0
for i in range(1, len(grid) - 2):
    for j in range(1, len(grid[i]) - 2):
        param = calculateAlignmentParameter(i, j, grid)
        print(param, end="")
        sum += param
    print("\n")
print(sum)


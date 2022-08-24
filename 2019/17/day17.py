from intcode import Computer

inp = list(map(int, open("2019/17/input.txt", "r").read().strip().split(",")))
intcode = Computer(inp)

grid = []
row = []
for i in range(0,2029):
    num = intcode.run_int_code([])

    if num == 10:
        grid.append(row)
        row = []
    else:
        row.append(chr(num))

# for line in grid:
#     print(''.join(line))
from intcode import Computer

inp = list(map(int, open("2019/17/input.txt", "r").read().strip().split(",")))
intcode = Computer(inp)


class Scaffolding:
    SCAFFOLDING = "#"

    def __init__(self, int_computer, input):
        grid = []
        row = []
        while True:
            num = int_computer.run_int_code([])
            if num == 10:
                grid.append(row)
                row = []
            elif num is None:
                break
            else:
                row.append(chr(num))
        self.grid = grid

    def print_grid(self):
        for line in grid:
            print(''.join(line))

    def isIntersection(self, i, j):
        return (self.grid[i][j] == self.SCAFFOLDING and 
                self.grid[i - 1][j] == self.SCAFFOLDING and 
                self.grid[i + 1][j] == self.SCAFFOLDING and 
                self.grid[i][j + 1] == self.SCAFFOLDING and 
                self.grid[i][j - 1] == self.SCAFFOLDING)

    def calculateAlignmentParameter(self, i, j):
        if self.isIntersection(i, j):
            return i * j
        else:
            return 0

    def calculate_sum_of_alignment_parameters(self):
        sum = 0
        for i in range(1, len(self.grid) - 2):
            for j in range(1, len(self.grid[i]) - 2):
                param = self.calculateAlignmentParameter(i, j)
                sum += param
        return sum

scaffolding = Scaffolding(intcode, inp)
print(scaffolding.calculate_sum_of_alignment_parameters())


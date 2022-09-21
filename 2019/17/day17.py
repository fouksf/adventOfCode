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
                if(chr(num)) == '^':
                    start_row = len(grid)
                    start_col = len(row)
        self.grid = grid

    def print_grid(self):
        for line in self.grid:
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

        # current orientation can be N, S, E, W
        # return value can be L or R
    def determine_direction_to_turn(self, x, y, old_x, old_y, current_orientation):
        if x + 1 <= len(self.grid[0]) and self.grid[x + 1][y] == SCAFFOLDING:
            if current_orientation == 'N':
                return 'R'
            elif current_orientation == 'S':
                return 'L'
            throw Exception("wtf")
        if x - 1 <= len(self.grid[0]) and self.grid[x - 1][y] == SCAFFOLDING:
            if current_orientation == 'N':
                return 'L'
            elif current_orientation == 'S':
                return 'R'
            throw Exception("wtf 2")
        if y + 1 <= len(self.grid[0]) and self.grid[x][y + 1] == SCAFFOLDING:
            if current_orientation == 'E':
                return 'R'
            elif current_orientation == 'W':
                return 'L'
            throw Exception("wtf 3")
        if y - 1 <= len(self.grid[0]) and self.grid[x][y - 1] == SCAFFOLDING:
            if current_orientation == 'W':
                return 'R'
            elif current_orientation == 'E':
                return 'L'
            throw Exception("wtf 4")

    def is_scaffolding(self, x, y):
        return self.grid[x][y] == SCAFFOLDING

    def determine_lenght_forward(self, x, y, orientation):
        delta = 1 if orientation == 'E' or orientation == 'N' else -1
        if orientation == 'N' or orientation = 'S':
            dy = y + delta
            while self.is_scaffolding(x, dy):
                dy += delta
            return (dy - y) * delta

        

    def find_path_commands(self):
        direction = determine_direction_to_turn()
        # // determine how far we can go
        # // repeat but exclude the direction we came from
        # end when there is no other place to go except back


scaffolding = Scaffolding(intcode, inp)
print(scaffolding.calculate_sum_of_alignment_parameters())
scaffolding.print_grid()


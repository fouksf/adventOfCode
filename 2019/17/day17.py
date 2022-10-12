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
        self.grid = grid[:-1]

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
    def determine_direction_to_turn(self, position, current_orientation):
        (x, y) = position
        if x + 1 <= len(self.grid[0]) and self.grid[x + 1][y] == self.SCAFFOLDING and not self.came_from(position, current_orientation, (x + 1, y)):
            if current_orientation == 'E':
                return ('R', 'S')
            elif current_orientation == 'W':
                return ('L', 'S')
            raise Exception("wtf")
        if x - 1 <= len(self.grid[0]) and self.grid[x - 1][y] == self.SCAFFOLDING and not self.came_from(position, current_orientation, (x - 1, y)):
            if current_orientation == 'W':
                return ('R', 'N')
            elif current_orientation == 'E':
                return ('L', 'N')
            raise Exception("wtf 2")
        if y + 1 <= len(self.grid[0]) and self.grid[x][y + 1] == self.SCAFFOLDING and not self.came_from(position, current_orientation, (x, y + 1)):
            if current_orientation == 'N':
                return ('R', 'E')
            elif current_orientation == 'S':
                return ('L', 'E')
            raise Exception("wtf 3")
        if y - 1 <= len(self.grid[0]) and self.grid[x][y - 1] == self.SCAFFOLDING and not self.came_from(position, current_orientation, (x, y - 1)):
            if current_orientation == 'N':
                return ('L', 'W')
            elif current_orientation == 'S':
                return ('R', 'W')
            raise Exception("wtf 4")
        raise Exception("wtf 5")

    def came_from(self, current_position, orientation, point_to_check):
        (x, y) = current_position
        (x1, y1) = point_to_check
        if orientation == 'E':
            return x == x1 and y - 1 == y1
        if orientation == 'W':
            return x == x1 and y + 1 == y1
        if orientation == 'S':
            return x - 1 == x1 and y == y1
        if orientation == 'N':
            return x + 1 == x1 and y == y1
        

    def is_scaffolding(self, x, y):
        return False if y >= len(self.grid[0]) or x > len(self.grid) else self.grid[x][y] == self.SCAFFOLDING

    def determine_length_forward(self, position, orientation):
        (x, y) = position
        delta = 1 if orientation == 'E' or orientation == 'S' else -1
        if orientation == 'E' or orientation == 'W':
            dy = y + delta
            while dy >= 0 and dy < len(self.grid[0]) and self.is_scaffolding(x, dy):
                dy += delta
            return (dy - y - delta) * delta
        else:
            dx = x + delta
            while dx >= 0 and dx < len(self.grid) and self.is_scaffolding(dx, y):
                dx += delta
            return (dx - x - delta) * delta
    
    def move(self, position, orientation, distance):
        (x, y) = position
        if orientation == 'N':
            return (x - distance, y)
        
        if orientation == 'S':
            return (x + distance, y)

        if orientation == 'E':
            return (x, y + distance)
        
        if orientation == 'W':
            return (x, y - distance)

        

    def find_path_commands(self):
        directions = []
        position = (16, 12)
        orientation = 'N'

        for x in range(0, 20):
            turn, orientation = self.determine_direction_to_turn(position, orientation)
            directions.append(turn)
            forward = self.determine_length_forward(position, orientation)
            directions.append(forward)
            # this should be updating
            position = self.move(position, orientation, forward)

        print(directions)
        # // determine how far we can go
        # // repeat but exclude the direction we came from
        # end when there is no other place to go except back


scaffolding = Scaffolding(intcode, inp)
scaffolding.print_grid()
# print(scaffolding.came_from((0,1), "E", (0,0)))
# print(scaffolding.came_from((0,0), "W", (0,1)))
# print(scaffolding.came_from((0,0), "N", (1,0)))
# print(scaffolding.came_from((1,0), "S", (0,0)))
# print(scaffolding.came_from((0,1), "W", (0,0)))
# print(scaffolding.came_from((0,0), "N", (0,1)))
# print(scaffolding.came_from((0,0), "S", (1,0)))
# print(scaffolding.came_from((1,0), "E", (0,0)))
# print(scaffolding.calculate_sum_of_alignment_parameters())
# scaffolding.print_grid()
scaffolding.find_path_commands()

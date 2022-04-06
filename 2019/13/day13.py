from intcode import Computer
from point import Point

input = list(map(int, open("2019/13/input.txt", "r").read().split(",")))

amplifier = Computer(input)

class ArcadeCabinet:
    def __init__(self):
        self.board = {}
        self.maxX = 0
        self.maxY = 0
        

    def draw_tile(self, x, y, tile_type):
        self.board[Point(x, y)] = tile_type
        self.maxX = max(self.maxX, x)
        self.maxY = max(self.maxY, y)

    def __repr__(self) -> str:
        grid = ""
        for row in range(self.maxX):
            for col in range(self.maxY):
                if Point(row, col) in self.board:
                    grid += self.tile_to_repr(self.board[Point(row, col)])
                else:
                    grid += "_"
            grid += "\n"
        return grid

    def tile_to_repr(self, tile):
        if tile == 0:
            return " "
        
        if tile == 1:
            return "X"
        
        if tile == 2:
            return "L"
        
        if tile == 3:
            return "_"

        if tile == 4:
            return "O"

cabinet = ArcadeCabinet()
score = 0
paddle_x = 0
inp = 0
while True:
    x = amplifier.run_int_code([inp])
    if x == None:
        break
    y = amplifier.run_int_code([])
    if x == -1 and y == 0:
        score = amplifier.run_int_code([])
    else:
        tile_type = amplifier.run_int_code([])
        if tile_type == 4:
            if paddle_x < x:
                inp = 1
            elif paddle_x > x:
                inp = -1
            else:
                inp = 0
        if tile_type == 3:
            paddle_x = x
            
        cabinet.draw_tile(y, x, tile_type)
        if tile_type == 4:
            print(cabinet)

print(score)


# print(cabinet)
# counter = 0
# for k, v in cabinet.board.items():
#     if v == 2:
#         counter += 1
# print(counter)
from intcode import Computer
from point import Point

input = list(map(int, open("2019/13/input.txt", "r").read().split(",")))

amplifier = Computer(input)

class ArcadeCabinet:
    def __init__(self):
        self.board = {}
        

    def draw_tile(self, x, y, tile_type):
        self.board[Point(x, y)] = tile_type


cabinet = ArcadeCabinet()

while True:
    x = amplifier.run_int_code([])
    if x == None:
        break
    y = amplifier.run_int_code([])
    tile_type = amplifier.run_int_code([])
    cabinet.draw_tile(x, y, tile_type)

counter = 0
for k, v in cabinet.board.items():
    if v == 2:
        counter += 1

    
print(counter)
from intcode import Computer
from point import Point
from collections import defaultdict

input = list(map(int, open("2019/11/input.txt", "r").read().split(",")))
# input = [104,1125899906842624,99]
amplifier = Computer(input)

BLACK = 0
WHITE = 1

LEFT_90 = 0
RIGHT_90 = 1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class PainterRobot:
    def __init__(self):
        self.is_first_position = True
        self.direction = UP
        self.position = Point(0, 0)
        self.painted_points = {}

    def turn(self, direction):
        if direction == LEFT_90:
            self.direction = (self.direction - 1) % 4
        elif direction == RIGHT_90:
            self.direction = (self.direction + 1) % 4
        else:
            print("Mayday mayday")

    def step(self):
        if self.direction == UP:
            self.position = Point(self.position.x, self.position.y - 1)
        elif self.direction == DOWN:
            self.position = Point(self.position.x, self.position.y + 1)
        elif self.direction == LEFT:
            self.position = Point(self.position.x - 1, self.position.y)
        elif self.direction == RIGHT:
            self.position = Point(self.position.x + 1, self.position.y)
        else:
            print("Huston, we have a problem!")
    
    def move(self, direction):
        self.turn(direction)
        self.step()

    def position_has_been_painted(self):
        return self.position in self.painted_points
    
    def get_current_position_colour(self):
        if self.is_first_position:
            self.is_first_position = False
            return WHITE
        if self.position_has_been_painted():
            return self.painted_points[self.position]
        return BLACK

    def paint_position(self, colour):
        self.painted_points[self.position] = colour
    
    
painter = PainterRobot()

while True:
    
    current_colour = painter.get_current_position_colour()
    
    new_colour = amplifier.run_int_code([current_colour])

    if (new_colour == None):
        break
    
    painter.paint_position(new_colour)

    direction_to_turn = amplifier.run_int_code([])
    painter.move(direction_to_turn)


print(len(painter.painted_points))


for j in range(7):
    result = ''
    for i in range(45):
        point = Point(i, j)
        if point in painter.painted_points:
            colour = painter.painted_points[point]
            if(colour == BLACK):
                result += "_"
            else:
                result += "#"
        else:
            result += "#"
    print(result)
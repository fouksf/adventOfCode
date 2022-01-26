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

current_point = Point(0, 0)
direction = UP
points_visited = {}

def move(turn, current_point):
    if turn == 0:
        direction = (direction + 1) % 4
    elif turn == 1:
        direction = (direction - 1) % 4
    
# TODO return new point based upon the new direction
    

    return current_point

while True:
    current_colour = BLACK

    if current_point in points_visited:
        current_colour = points_visited[current_point]
    
    new_colour = amplifier.run_int_code([current_colour])

    if (new_colour == None):
        break
    
    points_visited[current_point] = new_colour

    direction = amplifier.run_int_code([current_colour])
    current_point = move(direction, current_point)

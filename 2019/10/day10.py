import math

# input = open("2019/10/input.txt", "r").read()

input = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####'''

map_matrix = list(map(list, input.split("\n")))

# . is empty
# # is an asteroid
# top left corner is 0,0

points = []

for i, line in enumerate(map_matrix):
    for j, point in enumerate(line):
        if (point == '#'):
            points.append((i, j))


def calc_distance(point_one, point_two):
    (x, y) = point_one
    (a, b) = point_two

    return math.sqrt((x - a)**2 + (y - b)**2)

print(points)

def calc_visible_astroids():
    a = points[0]
    # for i, point in enumerate(points[1:]):

    b = points[1]
    c = points[2]

    a_b = calc_distance(a, b)
    a_c = calc_distance(a, c)
    b_c = calc_distance(b, c)

    if (a_b + b_c == a_c):
        if (a_b < a_c):
            points.pop(1)
        else:
            points.pop(2)
        
        
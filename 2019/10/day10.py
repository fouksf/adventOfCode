import math

# input = open("2019/10/input.txt", "r").read()

# input = '''......#.#.
# #..#.#....
# ..#######.
# .#.#.###..
# .#..#.....
# ..#....#.#
# #..#....#.
# .##.#..###
# ##...#..#.
# .#....####'''

input = '''.#..#
.....
#####
....#
...##'''

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

def calc_visible_astroids():
    a = points[0]
    # sorted_points = sorted(points, key=lambda point: calc_distance(point, a))
    # for i, point in enumerate(sorted_points[1:]):
    for i in range(0, len(points)-1):
        current_point = points[i]
        max_x = max(a[0], current_point[0])
        max_y = max(a[1], current_point[1])
        min_x = min(a[0], current_point[0])
        min_y = min(a[1], current_point[1])

        in_box = list(filter(lambda p1: p1[0] > min_x and p1[1] > min_y and p1[0] < max_x and p1[1] < max_y , points))

        for j in range(0, len(in_box)-1):
            if j == i:
                continue

            b = points[i]
            c = points[j]

            a_b = calc_distance(a, b)
            a_c = calc_distance(a, c)
            b_c = calc_distance(b, c)

            if (a_b + b_c == a_c):
                print(i)
                if (a_b < a_c):
                    points.pop(i)
                else:
                    points.pop(j)
    # we want 7
    return len(points)
        
print(calc_visible_astroids());
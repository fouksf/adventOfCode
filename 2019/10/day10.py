import math

input = open("2019/10/input.txt", "r").read()

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

# input = '''.#..#
# .....
# #####
# ....#
# ...##'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return self.x == other.x and self.y == other.y
        else:
            return False
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'

map_matrix = list(map(list, input.split("\n")))

# . is empty
# # is an asteroid
# top left corner is 0,0

points = []

for i, line in enumerate(map_matrix):
    for j, point in enumerate(line):
        if (point == '#'):
            points.append(Point(j, i))


def are_points_collinear(a: Point, b: Point, c: Point):
    if (a.x == b.x or b.x == c.x or a.x == c.x):
        return a.x == b.x == c.x
    slope_ab =(b.y - a.y)/(b.x - a.x)
    slobe_bc = (c.y - b.y)/(c.x - b.x)
    return slobe_bc == slope_ab


def calc_visible_astroids_for_point(a: Point):
    visible_points_count = len(points) - 1
    for i in range(0, len(points)):
        b = points[i]
        if (a == b):
            continue

        max_x = max(a.x, b.x)
        max_y = max(a.y, b.y)
        min_x = min(a.x, b.x)
        min_y = min(a.y, b.y)

        ab_rectangle = list(filter(lambda p: p.x >= min_x and p.y >= min_y and p.x <= max_x and p.y <= max_y, points))
        for j in range(0, len(ab_rectangle)-1):
            c = ab_rectangle[j]
            if a == c or b == c:
                continue

            if (are_points_collinear(a, b, c)):
                visible_points_count -= 1
                break
    return visible_points_count

def get_visible_asteroids():
    counts = {}
    for point in points:
        counts[point] = calc_visible_astroids_for_point(point)
    return counts

def find_most_visible_asteroids():
    max_visible = 0
    for point in points:
        current_visible = calc_visible_astroids_for_point(point)
        if (current_visible > max_visible):
            max_visible = current_visible
    return max_visible
        
print(find_most_visible_asteroids())

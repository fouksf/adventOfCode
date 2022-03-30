from collections import defaultdict

input = open("2021/5/input.txt", "r").read().split("\n")

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

class Line:
    def __init__(self, a: Point, b: Point):
        self.points = []
        if a.x == b.x:
            for y in range(min(a.y, b.y), max(a.y, b.y) + 1):
                self.points.append(Point(a.x, y))
        elif a.y == b.y:
            for x in range(min(a.x, b.x), max(a.x, b.x) + 1):
                self.points.append(Point(x, a.y))
        else:
            x_step = 1 if a.x < b.x else -1
            y_step = 1 if a.y < b.y else -1
            current = a
            while current != b:
                self.points.append(current)
                current = Point(current.x + x_step, current.y + y_step)
            self.points.append(b)


def read_input(input):
    lines = []
    for line in input:
        strings = line.split(' -> ')
        chars = list(map(lambda string: string.split(','), strings))
        ints = list(map(lambda charz: list(map(lambda a: int(a), charz)), chars))
        points = list(map(lambda intz: Point(intz[0], intz[1]), ints))
        lines.append(Line(points[0], points[1]))
    return lines

def find_overlapping_points(lines):
    points = {}
    for line in lines:
        for point in line.points:
            if point in points:
                points[point] += 1
            else:
                points[point] = 1
    
    counts = 0
    for i, point in enumerate(points):
        if points[point] > 1:
            counts += 1
    return counts


print(find_overlapping_points(read_input(input)))

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

def parse_input(file_name):
    (coordinates, folding_instructions) = open(file_name, "r").read().split('\n\n')
    points = set(
        map(
            lambda l: Point(int(l.split(',')[0]), 
                            int(l.split(',')[1])), 
            coordinates.split('\n')))
    folds = list(map(lambda i: i.split()[-1].split('='), folding_instructions.split('\n')))
    return (points, folds) 

def calculate_coord(coord, fold_line):
    return fold_line - (coord - fold_line)

def fold_vertical(points, line):
    return set(
        map(
            lambda point: point if point.x < line else Point(calculate_coord(point.x, line), point.y), 
            points))

def fold_horizontal(points, line):
    return set(
        map(
            lambda point: point if point.y < line else Point(point.x, calculate_coord(point.y, line)), 
            points))     

def print_points(points):
    output = ''
    for i in range(0, max(map(lambda p: p.y, points)) + 1):
        for j in range(0, max(map(lambda p: p.x, points)) + 1):
            if Point(j, i) in points:
                output += '#'
            else:
                output += '.'
        output += '\n'
    print(output)



(points, folds) = parse_input("2021/13/input.txt")
print_points(points)
for fold in folds:
    if fold[0] == 'x':
        points = fold_vertical(points, int(fold[1]))
    else:
        points = fold_horizontal(points, int(fold[1]))
    print_points(points)
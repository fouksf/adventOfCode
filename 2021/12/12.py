input = open("2021/12/input.txt", "r").read().split("\n")

class Vertex:
    def __init__(self, name):
        self.name = name
        self.is_big = name.isupper()
        self.can_visit_again = True
        self.neighbours = []

    def visit(self):
        if not self.is_big:
            self.can_visit_again = False
    def __repr__(self):
        return f'{self.name} -> {", ".join(self.neighbours)}'

def parse_input(input):
    graph = {}
    for line in input:
        (fromVertex, toVertex) = line.split('-')
        if fromVertex not in graph:
            graph[fromVertex] = Vertex(fromVertex)
        if toVertex not in graph:
            graph[toVertex] = Vertex(toVertex)
        graph[fromVertex].neighbours.append(toVertex)
        graph[toVertex].neighbours.append(fromVertex)
    return graph

def print_all_paths_helper(graph, currentVertex, end, path, paths, has_used_bonus):
    graph[currentVertex].visit()
    path.append(currentVertex)

    if currentVertex == end:
        # print(path)
        paths.append(path.copy())
    else:
        for neighbour in graph[currentVertex].neighbours:
            if graph[neighbour].can_visit_again:
                print_all_paths_helper(graph, neighbour, end, path, paths, has_used_bonus)
            elif not has_used_bonus and neighbour != 'start' and neighbour != 'end':
                print_all_paths_helper(graph, neighbour, end, path, paths, True)

    path.pop()
    if currentVertex not in path:
        graph[currentVertex].can_visit_again = True


def print_all_paths(graph, start, end):
    path = []
    paths = []
    print_all_paths_helper(graph, start, end, path, paths, False)
    print(len(paths))

print_all_paths(parse_input(input), 'start', 'end')
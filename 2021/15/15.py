from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any
import copy

@dataclass(order=True)
class PrioritizedItem:
    risk: int
    point: Any=field(compare=False)

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

class Vertex:
    def __init__(self, point, risk):
        self.point = point
        self.risk = risk
        self.visited = False

    def visit(self):
        self.visited = True


    def unvisit(self):
        self.visited = False

    def __repr__(self):
        return f'{self.point}, {self.visited}'


def parse_input(file_name):
    input = list(map(lambda l: list(map(int, list(l))), open(file_name, "r").read().split('\n')))
    big_input = copy.deepcopy(input)
    for _ in range(4 * len(input)):
        big_input.append([])
    for i in range(1, 9):
        input = list(map(lambda line: list(map(lambda n: n + 1 if n < 9 else 1, line)), input))
        for j in range(0, len(big_input)):
            if len(big_input[j]) < len(big_input) and j // len(input) <= i:
                big_input[j].extend(input[j % len(input)])

    risk_map = {}
    for i in range(0, len(big_input)):
        for j in range(0, len(big_input[0])):
            point = Point(j, i)
            risk_map[point] = Vertex(point, big_input[j][i])
    return (risk_map, len(big_input), len(big_input[0]))



def try_dijkstra(risk_map, start, maxX, maxY):
    risks = {v:float('inf') for v in risk_map.keys()}
    risks[start] = 0

    priorityQueue = PriorityQueue()
    priorityQueue.put(PrioritizedItem(0, start))

    while not priorityQueue.empty():
        current_vertex = priorityQueue.get().point
        
        risk_map[current_vertex].visit()

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if (current_vertex.x + dx < maxX and current_vertex.x + dx >= 0 and current_vertex.y + dy < maxY and current_vertex.y + dy >= 0):
                neighbour = Point(current_vertex.x + dx, current_vertex.y + dy)
                if not risk_map[neighbour].visited:
                    old_risk = risks[neighbour]
                    new_risk = risks[current_vertex] + risk_map[neighbour].risk
                    if new_risk < old_risk:
                        priorityQueue.put(PrioritizedItem(new_risk, neighbour))
                        risks[neighbour] = new_risk
    return risks

(risk_map, maxX, maxY) = parse_input("2021/15/input.txt")
print(try_dijkstra(risk_map, Point(0, 0), maxX, maxY))
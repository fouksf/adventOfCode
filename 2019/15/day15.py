from intcode import Computer
from point import Point
from copy import deepcopy

input = list(map(int, open("2019/15/input.txt", "r").read().split(",")))

class RepairDroid:
    def __init__(self, amplifier):
        self.found = False
        self.queue = [{
            'point': Point(0, 0),
            'steps': 0,
            'amp': amplifier
        }]
        self.visited = set()
        self.directionMapping = {
            1: self.get_northern_point,
            2: self.get_southern_point,
            4: self.get_eastern_point,
            3: self.get_western_point,
        }

    def reveal_map(self):
        while not self.found:
            current = self.queue.pop()

            if current['point'] in self.visited:
                continue

            self.visited.add(current['point'])
            steps = current['steps'] + 1

            for direction in range(1,5):
                newPoint = self.directionMapping[direction](current['point'])
                newIntCode = deepcopy(current['amp'])
                out = newIntCode.run_int_code([direction])
                # print(out)
                if out == 2:
                    self.found = True
                    print(steps)
                elif out == 0:
                    self.visited.add(newPoint)
                else:
                    # print("in here")
                    self.queue.append({'point': newPoint, 'steps': steps, 'amp': newIntCode})
                
                # print(self.queue)
            

    def get_northern_point(self, point):
        return Point(point.x, point.y + 1)

    def get_southern_point(self, point):
        return Point(point.x, point.y - 1)

    def get_eastern_point(self, point):
        return Point(point.x + 1, point.y)

    def get_western_point(self, point):
        return Point(point.x - 1, point.y)

intcode = Computer(input)
droid = RepairDroid(intcode)
droid.reveal_map()
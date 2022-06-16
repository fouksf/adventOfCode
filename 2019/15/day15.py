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
        self.max_steps = 0

    def go_to_o(self):
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
                    return newIntCode
                elif out == 0:
                    self.visited.add(newPoint)
                else:
                    # print("in here")
                    self.queue.append({'point': newPoint, 'steps': steps, 'amp': newIntCode})
                # print(self.queue)
            
    def time_oxygenation(self):
        while len(self.queue) > 0:
            current = self.queue.pop()

            if current['point'] in self.visited:
                continue

            self.visited.add(current['point'])
            steps = current['steps'] + 1

            if steps > self.max_steps:
                self.max_steps = steps

            for direction in range(1,5):
                newPoint = self.directionMapping[direction](current['point'])
                newIntCode = deepcopy(current['amp'])
                out = newIntCode.run_int_code([direction])
                
                if out == 0:
                    self.visited.add(newPoint)
                else:
                    self.queue.append({'point': newPoint, 'steps': steps, 'amp': newIntCode})
        
        print(self.max_steps - 1)


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
amp_at_o = droid.go_to_o()

time_droid = RepairDroid(amp_at_o).time_oxygenation()

from intcode import Computer
from point import Point

## reveal the graph by dfs
## breath first search to find the fastes way


repairDroid = Computer(input)

class RepairDroid:
    def __init__(self, amplifier):
        self.amp = amplifier
        self.graph = {} # (3,0) -> ./D/#/O
        self.instructions = []
        self.current_position = Point(0, 0)
        self.found = False
        self.queue = [{
            'point': Point(0, 0),
            'steps': 0,
        }]
        self.visited = {}


        self.directionMapping = {
            1: self.get_northern_point,
            2: self.get_southern_point,
            3: self.get_eastern_point,
            4: self.get_western_point,
        }

    def reveal_map(self):
        while not self.Found:
            current = self.queue.pop()

            if current.point in self.visited:
                continue

            self.visited.add(current['point'])
            steps = current.steps + 1

            for direction in range(1,5):
                newPoint = self.directionMapping[direction](current.point)
                newIntCode = self.amp.clone()

                out = newIntCode.run(direction)

                if out == 2:
                    print(steps)
                elif out == 0:
                    self.visited.add(newPoint)
                else:
                    self.queue.push({'point': newPoint, 'steps': steps})

    def get_northern_point(self):
        return Point(self.current_position.x, self.current_position.y + 1)

    def get_southern_point(self):
        return Point(self.current_position.x, self.current_position.y - 1)

    def get_eastern_point(self):
        return Point(self.current_position.x + 1, self.current_position.y)

    def get_western_point(self):
        return Point(self.current_position.x - 1, self.current_position.y)
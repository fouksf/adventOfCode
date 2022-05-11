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

    def reveal_map(self):
        while True:
            # check if already visited and try going N
            for direction in range(1,5):
            # if yes recursive
            # else check if already visited and if not try E, S, W
            # if cannot move to either direction go opposite last intrustion in instructions and continue from there

    def get_northern_point(self):
        return Point(self.current_position.x, self.current_position.y + 1)

    def get_southern_point(self):
        return Point(self.current_position.x, self.current_position.y - 1)

    def get_eastern_point(self):
        return Point(self.current_position.x + 1, self.current_position.y)

    def get_western_point(self):
        return Point(self.current_position.x - 1, self.current_position.y)
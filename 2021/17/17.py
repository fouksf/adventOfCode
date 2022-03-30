
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

class TargetArea:
    def __init__(self, minX, maxX, minY, maxY):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY
    

class ProbeLauncher:
    def __init__(self, velocity, target_area):
        self.position = Point(0, 0)
        self.velocity = velocity
        self.target_area = target_area
        self.trajectory = [self.position]
    
    def step(self):
        self.position = Point(self.position.x + self.velocity.x, self.position.y + self.velocity.y)
        self.trajectory.append(self.position)
        dx = 0
        if self.velocity.x < 0:
            dx = 1
        elif self.velocity.x > 0:
            dx = -1
        self.velocity = Point(self.velocity.x + dx, self.velocity.y - 1)
    
    def is_in_target_area(self):
        return (self.position.x >= self.target_area.minX and 
                self.position.x <= self.target_area.maxX and 
                self.position.y >= self.target_area.minY and 
                self.position.y <= self.target_area.maxY)
    
    def has_passed_the_target(self):
        return (self.position.x > self.target_area.maxX or
                self.position.y < self.target_area.minY)


targetArea = TargetArea(253, 280, -73, -46)
launcher = ProbeLauncher(Point(17,-4), targetArea)
def reaches_target_area(launcher):
    while not launcher.has_passed_the_target():
        launcher.step()
        if launcher.is_in_target_area():
            return True
    return False

max_height = -73
for x in range(1, 280):
    for y in range(-73, 1000):
        velocity = Point(x, y)
        launcher = ProbeLauncher(velocity, targetArea)
        if reaches_target_area(launcher):
            print(f'{velocity} reaches at y={y}')
            if y > max_height:
                max_height = y
        # else:
            # print(f'{velocity} does not reach the target area')


print(max_height)
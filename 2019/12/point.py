class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f'<x={self.x}, y={self.y}, z={self.z}>'
    
    def apply_velocity(self, velocity):
        self.x += velocity.x
        self.y += velocity.y
        self.z += velocity.z
    
    def energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
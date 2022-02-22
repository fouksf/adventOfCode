from velocity import Velocity

class Moon:
    def __init__(self, point):
        self.point = point
        self.velocity = Velocity(0, 0, 0)
    
    def __repr__(self):
        return f'pos={self.point}, vel={self.velocity}'
    
    def apply_gravity(self, other_moon):
        if (self.point.x > other_moon.point.x):
            self.velocity.x -= 1
        elif (self.point.x < other_moon.point.x):
            self.velocity.x += 1
        
        if (self.point.y > other_moon.point.y):
            self.velocity.y -= 1
        elif (self.point.y < other_moon.point.y):
            self.velocity.y += 1
        
        if (self.point.z > other_moon.point.z):
            self.velocity.z -= 1
        elif (self.point.z < other_moon.point.z):
            self.velocity.z += 1
    
    def apply_velocity(self):
        self.point.apply_velocity(self.velocity)
    
    def get_energy(self):
        return self.point.energy() * self.velocity.energy()
from velocity import Velocity

class Moon:
    def __init__(self, point):
        self.point = point
        self.velocity = Velocity(0, 0, 0)
        self.states = [self.__repr__()]
        self.orbit_time = None
        self.initial_point = point
        self.initial_velocity = velocity
    
    def __repr__(self):
        return f'pos={self.point}, vel={self.velocity}'

    def x_is_same_as_initial(self):
        return self.point.x == self.initial_point.x and self.velocity.x == self.initial_velocity.x

    def y_is_same_as_initial(self):
        return self.point.y == self.initial_point.y and self.velocity.y == self.initial_velocity.y

    def z_is_same_as_initial(self):
        return self.point.z == self.initial_point.z and self.velocity.z == self.initial_velocity.z
    
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
        
    def record_state(self):
        if self.__repr__() in self.states:
            self.orbit_time = len(self.states)
            print(self.orbit_time)
        else:
            self.states.append(self.__repr__())
    
    def apply_velocity(self):
        self.point.apply_velocity(self.velocity)
        if self.orbit_time == None:
            self.record_state()
    
    def get_energy(self):
        return self.point.energy() * self.velocity.energy()
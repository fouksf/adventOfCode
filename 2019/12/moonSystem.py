def class MoonSystem:
    def __init__(self, moons):
        self.moons = moons
        self.x_period = None
        self.y_period = None
        self.z_period = None
        self.turn = 0

    def tick(self):
        for this_moon in self.moons:
            for other_moon in self.moons:
                if (this_moon == other_moon):
                    continue
                
                this_moon.apply_gravity(other_moon)
        
        for moon in self.moons:
            moon.apply_velocity()
        
        self.turn += 1

    def find_cycle(self):
        while not (self.x_period and self.y_period and self.z_period):
            self.tick()
            if not self.x_period and moon[0].x_is_same_as_initial() and moon[1].x_is_same_as_initial() and moon[2].x_is_same_as_initial() and moon[3].x_is_same_as_initial():
                self.x_period = self.turn
            if not self.y_period and moon[0].y_is_same_as_initial() and moon[1].y_is_same_as_initial() and moon[2].y_is_same_as_initial() and moon[3].y_is_same_as_initial():
                self.y_period = self.turn
            if not self.z_period and moon[0].z_is_same_as_initial() and moon[1].z_is_same_as_initial() and moon[2].z_is_same_as_initial() and moon[3].z_is_same_as_initial():
                self.z_period = self.turn
        return abs(self.x_period * self.y_period * self.x_period) // math.gcd(self.x_period, self.y_period, self.z_period)
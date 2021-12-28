class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        Vehicle.__init__(self,name, max_speed, mileage)

Sc= Bus("vacation", 200, 45)
print( Sc.name, Sc.max_speed, Sc.mileage)
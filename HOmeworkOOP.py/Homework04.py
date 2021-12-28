class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
    

Sc = Bus("School Volvo", 180, 12)
print("Vehicle Name:", Sc.name, "Speed:", Sc.max_speed, "Mileage:", Sc.mileage)
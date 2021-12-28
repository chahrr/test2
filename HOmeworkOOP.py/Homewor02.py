class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
        
car = Vehicle(220, 10000)
print(car.max_speed, car.mileage)
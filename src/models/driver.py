from models.car import Car


class Driver:
    name = ""
    age = None
    car = None

    def __init__(self, name: str, age: int, car: Car):
        self.name = name
        self.age = age
        self.car = car

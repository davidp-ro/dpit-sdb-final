from models.car import Car


class Driver:
    id = None
    name = ""
    age = None
    car = None

    def __init__(self, id: int, name: str, age: int, car: Car):
        self.id = id
        self.name = name
        self.age = age
        self.car = car

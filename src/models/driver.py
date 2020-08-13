from models.car import Car


class Driver:
    """
    Class for the drivers

    Args:
        id (int): Driver id
        name (str): Driver name
        age (int): Driver age
        car (Car or None): Car that is associated with the driver, None to leave blank
    """

    def __init__(self, id: int, name: str, age: int, car: Car or None) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.car = car

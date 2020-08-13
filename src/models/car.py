class Car:
    """
    Class for the cars

    Args:
        id (int): Car id
        reg (str): Car registration number
        brand (str): Car brand
        hp (int): Car horsepower
        kms (int): Car kms
    """

    def __init__(self, id: int, reg: str, brand: str, hp: int, kms: int) -> None:
        self.id = id
        self.reg = reg
        self.brand = brand
        self.hp = hp
        self.kms = kms

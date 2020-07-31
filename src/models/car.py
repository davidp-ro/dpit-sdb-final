class Car:
    id = None
    reg = ""
    brand = ""
    hp = None
    kms = None

    def __init__(self, id: int, reg: str, brand: str, hp: int, kms: int) -> None:
        self.id = id
        self.reg = reg
        self.brand = brand
        self.hp = hp
        self.kms = kms

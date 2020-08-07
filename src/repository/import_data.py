import json
from models.car import Car
from models.driver import Driver


def return_right_car(car_id: int, car_instance_list: list) -> Car or None:
    if car_id == -1:
        return None
    
    for car_ in car_instance_list:
        if car_.id == car_id:
            return car_

    return None


def import_data(car_instance_list: list, driver_instance_list: list) -> None:
    with open("data/cars.json", 'r') as cars_file:
        json_ = json.load(cars_file)
        cars_ = json_["cars"]
        for car_ in cars_:
            car_instance_list.append(
                Car(car_["id"],
                    car_["reg"],
                    car_["brand"],
                    car_["hp"],
                    car_["kms"])
            )

    with open("data/drivers.json", 'r') as drivers_file:
        json_ = json.load(drivers_file)
        drivers_ = json_["drivers"]
        for driver_ in drivers_:
            car_for_driver = return_right_car(driver_["car_id"], car_instance_list)

            driver_instance_list.append(
                Driver(
                    driver_["id"],
                    driver_["name"],
                    driver_["age"],
                    car_for_driver)
            )

import json

def save_data(mode: str = "complete", only: str = None, car_instance_list: list = None, driver_instance_list: list = None) -> None:
    """
    Save drivers/cars

    Args:
        mode (str, optional): "complete"/"single". Defaults to "complete".
        only (str, optional): If None saves all. Mandatory if mode=single Other options are "drivers" or "cars". Defaults to None.
        car_instance_list (list, optional): The instance list for cars. Defaults to None
        driver_instance_list (list, optional): The instance list for drivers. Defaults to None

    Raises:
        AttributeError: if given argument is incorrect
        ValueError: if car_instance_list or/and driver_instance_list were None when they needed to be valid

    Examples:
        save_data(car_instance_list=car_ent_list, driver_instance_list=driver_ent_list)) -> Will save everything
        save_data(only="cars", car_instance_list=car_ent_list) -> Will save from scratch, but only the cars
        save_data(mode="single", only="drivers", driver_instance_list=driver_ent_list) -> Will ONLY save the elements from the given entity_type 
    """
    if mode == "complete":
        # Complete mode:
        if car_instance_list is not None and driver_instance_list is not None:
            proccess_save_all(car_instance_list, driver_instance_list)
        else:
            # Wrong argument
            raise ValueError("In complete mode, both drivers and cars instance list must pe given as an argument (defaults to None)")
    elif mode == "single":
        # Append mode:
        if only == "cars":
            if car_instance_list is not None:
                proccess_save_car(car_instance_list)
            else:
                # Wrong argument
                raise ValueError("The car_instance_list must not be None")
        elif only == "drivers":
            if driver_instance_list is not None:
                proccess_save_driver(driver_instance_list)
            else:
                # Wrong argument
                raise ValueError("The driver_instance_list must not be None")
        else:
            # Wrong argument
            raise AttributeError("Invalid \"only\" argument! Valid args: drivers or cars")
    else:
        # Wrong argument
        raise AttributeError("Available modes: complete and single")


# Helpers:

def proccess_save_all(car_instance_list: list, driver_instance_list: list) -> None:
    """
    Helper for saving all data

    Args:
        car_instance_list (list): Car instance list
        driver_instance_list (list): Driver instance list
    """
    proccess_save_car(car_instance_list)
    proccess_save_driver(driver_instance_list)
    

def proccess_save_car(car_instance_list: list) -> None:
    """
    Helper for only saving car data

    Args:
        car_instance_list (list): Car instance list
    """
    # Save all cars:
    with open("data/cars.json", 'w') as cars_file:
        cars_ = []
        for car in car_instance_list:
            cars_.append(
                {
                    "id": car.id,
                    "reg": car.reg,
                    "brand": car.brand,
                    "hp": car.hp,
                    "kms": car.kms
                }
            )
        to_save = {"cars": cars_}
        json.dump(
            to_save,
            cars_file,
            indent=2
        )
        

def proccess_save_driver(driver_instance_list: list) -> None:
    """
    Helper for only saving driver data

    Args:
        driver_instance_list (list): Driver instance list
    """
    # Save all drivers
    with open("data/drivers.json", 'w') as drivers_file:
        drivers_ = []
        for driver in driver_instance_list:
            car_id = driver.car.id if driver.car is not None else -1
            drivers_.append(
                {
                    "id": driver.id,
                    "name": driver.name,
                    "age": driver.age,
                    "car_id": car_id,
                }
            )
        to_save = {"drivers": drivers_}
        json.dump(
            to_save,
            drivers_file,
            indent=2
        )
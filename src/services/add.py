from terminaltables import SingleTable
from utils.input_checker import Parser
from repository.repo import Repo
from repository.save_data import save_data
import ui.console_utils as console
import ui.one_line_table as olt
from models.car import Car
from models.driver import Driver


def handle_add_driver(driver_repo: Repo, parser: Parser, car_repo: Repo) -> None:
    """
    Handle adding a driver

    Args:
        driver_repo (Repo): Driver repository
        parser (Parser): Input data parser
        car_repo (Repo): Car repository
    """
    new_id = None
    new_name = ""
    new_age = None
    
    # Get driver id:
    done_id = False
    while not done_id:
        id_ = input("Enter driver id (numeric), leave blank for autocomplete > ")
        if id_ == "":
            _, last_entity = driver_repo.get(mode="last")
            id_ = last_entity.id
            found = False
            
            while not found:
                id_ += 1
                if not parser.check_if_already_exists(by_id=True, id=int(id_)):
                    found = True
                    new_id = int(id_)
                    done_id = True
                    print(f"\tAutocomplete succesfull, assigned id {new_id}")
        else:
            if not parser.check_if_already_exists(by_id=True, id=int(id_)):
                new_id = int(id_)
                done_id = True
            else:
                console.clear_console()
                olt.show(
                    title="Info",
                    message="This id already exists, you might want to auto-complete, just press enter",
                    go_back=False
                )

    # Get driver name:
    new_name = input("Enter the driver's name > ")

    # Get driver age:
    done_age = False
    while not done_age:
        age = input("Enter the driver's age (numeric) > ")
        try:
            new_age = int(age)
            done_age = True
        except ValueError:
            console.clear_console()
            olt.show(
                    title="Info",
                    message="The age must be a numeric value, ex: 45",
                    go_back=False
                )

    # Deal with car assignment:
    if input("Do you want to assign a car now? y/n > ").lower() == "y":
        # Add car:
        print("In order to assign a car to a driver you need it's ID, do you know it, or do you want to see all cars")
        input_ = input("Press enter to see all cars or enter an ID > ")
        if input_ == "":
            _, car_list = car_repo.get()
            if len(car_list) == 0 or car_list is None:
                olt.show(
                    title="Something went wrong",
                    message="Either there are no cars at this moment or something else went wrong"
                )
            else:
                table_data = [["ID", "Registration"]]
                for car in car_list:
                    table_data.append([str(car.id), car.reg])

                car_table = SingleTable(table_data, title="Cars")
                car_table.justify_columns = {
                    0: "left",
                    1: "center",
                }
                
                while True:
                    console.clear_console()
                    print(car_table.table)
                    input_ = input("Type b or back to go back > ")
                    if input_ == "b" or input_ == "back":
                        break
                    else:
                        continue

                console.clear_console()
                input_ = input("Enter car id or \"back\" if you want to leave it blank for now > ")
                if input_ == "back":
                    # Just add driver with no car assigned
                    driver_repo.add(Driver(new_id, new_name, new_age, None))
                else:
                    try:
                        new_car_id = int(input_)
                        resp, car_ = car_repo.get(mode="single", entity_id=new_car_id)
                        if resp == "found":
                            # Add driver with respective car
                            driver_repo.add(Driver(new_id, new_name, new_age, car_))
                        else:
                            olt.show(
                            title="Warning",
                            message="ID not found! Leaving blank for now, update via menu"
                            )
                            driver_repo.add(Driver(new_id, new_name, new_age, None))
                    except ValueError:
                        olt.show(
                            title="Warning",
                            message="The id must be numeric. Leaving blank for now, update via menu"
                        )
                        driver_repo.add(Driver(new_id, new_name, new_age, None))
        else:
            # User gave manual id:
            try:
                new_car_id = int(input_)
                resp, car_ = car_repo.get(mode="single", entity_id=new_car_id)
                if resp == "found":
                    # Add driver with respective car
                    driver_repo.add(Driver(new_id, new_name, new_age, car_))
                else:
                    olt.show(
                        title="Warning",
                        message="ID not found! Leaving blank for now, update via menu"
                    )
                    driver_repo.add(Driver(new_id, new_name, new_age, None))
            except ValueError:
                olt.show(
                    title="Warning",
                    message="The id must be numeric. Leaving blank for now, update via menu"
                )
                driver_repo.add(Driver(new_id, new_name, new_age, None))
    else:
        # Just add driver with no car assigned
        driver_repo.add(Driver(new_id, new_name, new_age, None))
    
    _, driver_instance_list = driver_repo.get()
    save_data(
        mode="single",
        only="drivers",
        driver_instance_list=driver_instance_list
    )
    olt.show(
        title="Success",
        message="The new driver was added succesfully"
    )


def handle_add_car(car_repo: Repo, parser: Parser):
    """
    Handle adding a car

    Args:
        car_repo (Repo): Car repository
        parser (Parser): Input parser
    """
    new_id = None
    new_reg = ""
    new_brand = ""
    new_hp = None
    new_kms = None

    # Get car id:
    done_id = False
    while not done_id:
        id_ = input("Enter car id (numeric), leave blank for autocomplete > ")
        if id_ == "":
            _, last_entity = car_repo.get(mode="last")
            id_ = last_entity.id
            found = False
            
            while not found:
                id_ += 1
                if not parser.check_if_already_exists(by_id=True, id=int(id_)):
                    found = True
                    new_id = int(id_)
                    done_id = True
                    print(f"\tAutocomplete succesfull, assigned id {new_id}")
        else:
            if not parser.check_if_already_exists(by_id=True, id=int(id_)):
                new_id = int(id_)
                done_id = True
            else:
                console.clear_console()
                olt.show(
                    title="Info",
                    message="This id already exists, you might want to auto-complete, just press enter",
                    go_back=False
                )

    # Get car registration:
    new_reg = input("Enter car registration no. > ").upper()

    # Get car brand:
    new_brand = input("Enter car brand > ")

    # Get car hp:
    done_hp = False
    while not done_hp:
        hp = input("Enter the car's horsepower (numeric) > ")
        try:
            new_hp = int(hp)
            done_hp = True
        except ValueError:
            console.clear_console()
            olt.show(
                    title="Info",
                    message="The horsepower must be a numeric value, ex: 105",
                    go_back=False
                )

    # Get car kms:
    done_kms = False
    while not done_kms:
        kms = input("Enter the car's current KMs (numeric) > ")
        try:
            new_kms = int(kms)
            done_kms = True
        except ValueError:
            console.clear_console()
            olt.show(
                    title="Info",
                    message="The current kilometers must be a numeric value, ex: 105",
                    go_back=False
                )

    car_repo.add(Car(new_id, new_reg, new_brand, new_hp, new_kms))
    _, car_instance_list = car_repo.get()
    save_data(
        mode="single",
        only="cars",
        car_instance_list=car_instance_list
    )
    olt.show(
        title="Success",
        message="The new car was added succesfully"
    )
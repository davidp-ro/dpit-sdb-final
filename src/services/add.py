from utils.input_checker import Parser
from repository.repo import Repo
from repository.save_data import save_data
import ui.console_utils as console
import ui.one_line_table as olt
from models.car import Car
from models.driver import Driver

def handle_add_driver(driver_repo: Repo, parser: Parser):
    new_id = None
    new_name = ""
    new_age = None
    
    # Get driver id:
    done_id = False
    while not done_id:
        id_ = input("Enter driver id (numeric), leave blank for autocomplete > ")
        if id_ is "":
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
                    message="The id already exists, you might want to auto-complete, just press enter",
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
                    message="This age must be a numeric value, ex: 45",
                    go_back=False
                )

    # Deal with car assignment:
    if input("Do you want to assign a car now? y/n > ").lower() == "y":
        # Add car:
        pass
    else:
        # Just add driver with no car assigned
        driver_repo.add(Driver(new_id, new_name, new_age, None))
        save_data()
        olt.show(
            title="Success",
            message="The new driver was added succesfully"
        )


def handler_add_car(car_repo: Repo, parser: Parser):
    pass
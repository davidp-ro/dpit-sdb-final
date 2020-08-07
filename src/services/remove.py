from terminaltables import SingleTable
from utils.input_checker import Parser
from repository.repo import Repo
from repository.save_data import save_data
import ui.console_utils as console
import ui.one_line_table as olt

def handle_remove_driver(driver_repo: Repo, parser: Parser):
    """
    Handle removing a driver

    Args:
        driver_repo (Repo): Driver repository
        parser (Parser): Input parser
    """
    # Get driver id:
    done_id = False
    _, driver_list = driver_repo.get()

    while not done_id:
        id_ = input("Enter driver id (numeric) or leave blank to see the driver list > ")
        if id_ == "":
            table_data = [["ID", "Name"]]
            for driver in driver_list:
                table_data.append([str(driver.id), driver.name])

            driver_table = SingleTable(table_data, title="Drivers")
            driver_table.justify_columns = {
                0: "left",
                1: "center",
            }
            while True:
                    console.clear_console()
                    print(driver_table.table)
                    input_ = input("Type b or back to go back > ")
                    if input_ == "b" or input_ == "back":
                        break
                    else:
                        continue
        else:
            try:
                id_ = int(id_)

                if parser.check_if_already_exists(by_id=True, id=id_):
                    # Id exists, continue:
                    done_id = True
                    driver_repo.delete(entity_id=id_)

                    save_data(
                        mode="single", 
                        only="drivers", 
                        driver_instance_list=driver_list
                    )
                    olt.show(
                        title="Success",
                        message="The driver was removed succesfully"
                    )
            except ValueError:
                console.clear_console()
                olt.show(
                    title="Info",
                    message="Invalid ID! The ID Must be numeric",
                    go_back=False
                )
            else:
                console.clear_console()
                olt.show(
                    title="Info",
                    message="Invalid ID!",
                    go_back=False
                )

def handle_remove_car(car_repo: Repo, parser: Parser):
    """
    Handle removing a car

    Args:
        car_repo (Repo): Car repository
        parser (Parser): Input parser
    """

    # Get car id:
    done_id = False
    _, car_list = car_repo.get()

    while not done_id:
        id_ = input("Enter car id (numeric) or leave blank to see the car list > ")
        if id_ == "":
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
        else:
            try:
                id_ = int(id_)

                if parser.check_if_already_exists(by_id=True, id=id_):
                    # Id exists, continue:
                    done_id = True
                    car_repo.delete(entity_id=id_)

                    save_data(
                        mode="single", 
                        only="cars", 
                        car_instance_list=car_list
                    )
                    olt.show(
                        title="Success",
                        message="The car was removed succesfully"
                    )
            except ValueError:
                console.clear_console()
                olt.show(
                    title="Info",
                    message="Invalid ID! The ID Must be numeric",
                    go_back=False
                )
            else:
                console.clear_console()
                olt.show(
                    title="Info",
                    message="Invalid ID!",
                    go_back=False
                )
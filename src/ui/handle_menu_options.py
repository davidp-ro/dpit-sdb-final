import os
from terminaltables import SingleTable
import ui.console_utils as console
from repository.repo import Repo
import ui.one_line_table as olt
from utils.input_checker import Parser
from services import add, update, remove


class Handler:
    car_instance_list = []
    driver_instance_list = []
        
    def __init__(self, car_instance_list: list, driver_instance_list: list):
        self.car_instance_list = car_instance_list
        self.driver_instance_list = driver_instance_list

    def show_drivers(self):
        driver_repo = Repo(self.driver_instance_list)
        response, driver_list = driver_repo.get(mode="all")

        if response is "found" and len(driver_list) is not 0:
            table_data = [["ID", "Name", "Age", "Car"]]
            for driver in driver_list:
                car_ = driver.car
                car_data = f"{car_.brand} with reg: {car_.reg}" if car_ is not None else "Driver does not have a car asociatted"
                table_data.append([str(driver.id), driver.name, str(driver.age), car_data])

            driver_table = SingleTable(table_data, title="Drivers")
            driver_table.justify_columns = {
                0: "left",
                1: "left",
                2: "left",
                3: "center"
            }
            
            while True:
                console.clear_console()
                print(driver_table.table)
                input_ = input("Type b or back to go back > ")
                if input_ == "b" or input_ == "back":
                    break
                else:
                    continue
        elif len(driver_list) is 0:
            olt.show(
                title="Info",
                message="No drivers! Either add using the menu or change the file"
            )
        else:
            olt.show(
                title="Something went wrong",
                message="Please try again"
                )


    def show_cars(self):
        car_repo = Repo(self.car_instance_list)
        response, car_list = car_repo.get(mode="all")

        if response is "found" and len(car_list) is not 0:
            table_data = [["ID", "Registration", "Brand", "HP", "KMs"]]
            for car in car_list:
                table_data.append([str(car.id), car.reg, car.brand, str(car.hp), str(car.kms)])
                # car_ = driver.car
                # car_data = f"{car_.brand} with reg: {car_.reg}" if car_ is not None else "Driver does not have a car asociatted"
                # table_data.append([str(driver.id), driver.name, str(driver.age), car_data])

            car_table = SingleTable(table_data, title="Cars")
            car_table.justify_columns = {
                0: "left",
                1: "center",
                2: "center",
                3: "left",
                4: "left"
            }
            
            while True:
                console.clear_console()
                print(car_table.table)
                input_ = input("Type b or back to go back > ")
                if input_ == "b" or input_ == "back":
                    break
                else:
                    continue
        elif len(car_list) is 0:
            olt.show(
                title="Info",
                message="No cars! Either add using the menu or change the file"
            )
        else:
            olt.show(
                title="Something went wrong",
                message="Please try again"
                )
    

    def add_driver(self):
        console.clear_console()
        olt.show(
            title="Add a driver",
            message="To add a new driver just complete all the details below",
            go_back=False
        )
        driver_repo = Repo(self.driver_instance_list)
        parser = Parser(driver_repo)
        add.handle_add_driver(driver_repo, parser)


    def add_car(self):
        console.clear_console()
        olt.show(
            title="Add a car",
            message="To add a new car just complete all the details below",
            go_back=False
        )
        car_repo = Repo(self.car_instance_list)
        parser = Parser(car_repo)
        add.handle_add_car(car_repo, parser)

    def remove_driver(self):
        console.clear_console()
        olt.show(
            title="Remove a driver",
            message="To remove a driver please complete the details below",
            go_back=False
        )
        driver_repo = Repo(self.driver_instance_list)
        parser = Parser(driver_repo)
        remove.handle_remove_driver(driver_repo, parser)

    def remove_car(self):
        console.clear_console()
        olt.show(
            title="Remove a car",
            message="To remove a car please complete the details below",
            go_back=False
        )
        car_repo = Repo(self.car_instance_list)
        parser = Parser(car_repo)
        remove.handle_remove_car(car_repo, parser)

    def update_driver(self):
        console.clear_console()
        olt.show(
            title="Update a driver",
            message="To update a driver just complete all the details below",
            go_back=False
        )
        driver_repo = Repo(self.driver_instance_list)
        parser = Parser(driver_repo)
        update.handle_update_driver(driver_repo, parser)

    def update_car(self):
        console.clear_console()
        olt.show(
            title="Update a car",
            message="To update a car just complete all the details below",
            go_back=False
        )
        car_repo = Repo(self.car_instance_list)
        parser = Parser(car_repo)
        update.handle_update_car(car_repo, parser)

    def show_statistics_menu(self):
        pass

    def show_about(self):
        olt.show(
            title="About",
            message="Made by David Pescariu for the final project within the SDB Course | <3 Academia Dpit | August 2020"
        )

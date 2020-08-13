from terminaltables import SingleTable
from ui.handle_menu_options import Handler
from ui.console_messages import stop
import ui.console_utils as console


class Menu:
    """
    Main Menu Class - Show options and react to chosen one

    Args:
        car_instance_list (list): Car instance list
        driver_instance_list (list): Dirver instance list
    """
    
    def __init__(self, car_instance_list: list, driver_instance_list: list):
        self.car_instance_list = car_instance_list
        self.driver_instance_list = driver_instance_list
        self.handler = Handler(self.car_instance_list, self.driver_instance_list)

        self.options_names = [
            ["Key", "Command"],  # Header
            ["1", "Show all drivers"],
            ["2", "Show all cars"],
            ["3", "Add a driver"],
            ["4", "Add a car"],
            ["5", "Remove a driver"],
            ["6", "Remove a car"],
            ["7", "Update a driver"],
            ["8", "Update a car"],
            ["9", "Statistics"],
            ["a", "About"],
            ["e", "Exit"],
        ]

        self.options = {
            "1": self.handler.show_drivers,
            "2": self.handler.show_cars,
            "3": self.handler.add_driver,
            "4": self.handler.add_car,
            "5": self.handler.remove_driver,
            "6": self.handler.remove_car,
            "7": self.handler.update_driver,
            "8": self.handler.update_car,
            "9": self.handler.show_statistics_menu,
            "a": self.handler.show_about,
        }

    def show_menu(self) -> None:
        """
        Show the menu
        """
        while True:
            console.clear_console()
            option_table = SingleTable(self.options_names, title="Main Menu")
            option_table.justify_columns = {
                0: "center",
                1: "left"
            }
            print(option_table.table)
            selected = input("> ")
            if selected == "e":
                stop()
                quit()
            else:
                try:
                    # React to option
                    self.options[selected]()
                except KeyError:
                    print("Invalid option!")
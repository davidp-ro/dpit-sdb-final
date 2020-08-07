from terminaltables import SingleTable
import ui.console_utils as console
from ui.handle_statistics_options import Handler


class StatisticsMenu:
    """
        This class contains the actual menu items that get printed and called for the
    statistics

    Methods:
        show: Show the menu
    """
    car_instance_list = []
    driver_instance_list = []
    handler = None
    options_names = []
    options = {}
    
    def __init__(self, car_instance_list: list, driver_instance_list: list) -> None:
        self.car_instance_list = car_instance_list
        self.driver_instance_list = driver_instance_list
        self.handler = Handler(car_instance_list, driver_instance_list)
        
        self.options_names = [
                ["Key", "Command"],  # Header
                ["1", "Avrage age of drivers"],
                ["2", "Show oldest and youngest driver"],
                ["3", "Show drivers with no cars"],
                ["4", "Show cars with no drivers"],
                ["5", "Most popular car brand"],
                ["6", "Avrage car kilometers"],
                ["7", "Avrage car horsepower"],
                ["b", "Go back to previous menu"]
            ]

        self.options = {
            "1": self.handler.avrage_age,
            "2": self.handler.oldest_youngest_driver,
            "3": self.handler.drivers_with_no_cars,
            "4": self.handler.cars_with_no_drivers,
            "5": self.handler.most_popular_brand,
            "6": self.handler.avrage_kms,
            "7": self.handler.avrage_hp
        }

    def show(self):
        option_table = SingleTable(self.options_names, title="Statistics")
        option_table.justify_columns = {
            0: "center",
            1: "left"
        }
        
        while True:
            console.clear_console()
            print(option_table.table)

            selected = input("> ")
            if selected == "b":
                break
            else:
                try:
                    print("selected", selected)
                    self.options[selected]()
                except KeyError:
                    print("Invalid option!")
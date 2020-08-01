import utils.handle_menu_options as handler
from ui.console_messages import stop

class Menu:
    car_instance_list = []
    driver_instance_list = []

    options_names = [
        "1. Show all drivers",
        "2. Show all cars",
        "3. Add a driver",
        "4. Add a car",
        "5. Remove a driver",
        "6. Remove a car",
        "7. Update a driver",
        "8. Update a car",
        "9. Statistics",
        "To exit type e or exit"
    ]

    options = {
        "1": handler.test()
    }

    def __init__(self, car_instance_list: list, driver_instance_list: list):
        self.car_instance_list = car_instance_list
        self.driver_instance_list = driver_instance_list

    def show_menu(self):
        while True:
            for option in self.options_names:
                print(option)
            selected = input("> ")
            if selected is "e" or selected is "exit":
                stop()
                quit()
            else:
                try:
                    self.options[selected]
                except KeyError:
                    print("Invalid option!")
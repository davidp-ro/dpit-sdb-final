"""
---------------------------------------------------------
    Entry point for the car/driver management app/project
  for the final task @ SDB - DPIT 2020

    See README for more details
---------------------------------------------------------
"""
__author__ = 'David Pescariu'
__version__ = '1.0'


def main():
    # Show start message
    from ui.console_messages import start
    start()

    # Check dependencies
    from utils.check_deps import check_imports
    check_imports()

    # Initailize our instance lists
    car_instance_list = []
    driver_instance_list = []

    # Get saved data from files
    from repository.import_data import import_data
    import_data(car_instance_list, driver_instance_list)

    # Begin showing menu
    from ui.console_menu import Menu
    menu = Menu(car_instance_list, driver_instance_list)
    menu.show_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Just in case we get a ctrl-c
        from ui.console_messages import stop
        stop()


"""
David Pescariu | August 2020 | MIT License | https://github.com/davidp-ro
"""

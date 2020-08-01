# David Pescariu ~ Aug 2020
# Final Project - SDB
#
# See README for details


def main():
    # Show start message
    from ui.console_messages import start
    start()

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

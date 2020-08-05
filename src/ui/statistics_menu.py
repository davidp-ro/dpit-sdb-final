class StatisticsMenu:
    car_instance_list = []
    driver_instance_list = []
    
    def __init__(self, car_instance_list: list, driver_instance_list: list) -> None:
        self.car_instance_list = car_instance_list
        self.driver_instance_list = driver_instance_list

    def show(self):
        while True:
            print("show")
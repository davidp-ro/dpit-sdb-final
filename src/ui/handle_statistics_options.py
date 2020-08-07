from terminaltables import SingleTable
import ui.console_utils as console
import ui.one_line_table as olt
from services.statistics import StatisticsService

class Handler:
    """
        This class contains all the handler(printing to the console) functions for 
    the statistics menu

    Methods:
        avrage_age
        oldest_youngest_driver
        drivers_with_no_cars
        cars_with_no_drivers
        most_popular_brand
        avrage_kms
        avrage_hp
    """
    car_instance_list = []
    driver_instance_list = []
    statisticsService = None
        
    def __init__(self, car_instance_list: list, driver_instance_list: list):
        self.car_instance_list = car_instance_list
        self.driver_instance_list = driver_instance_list
        self.statisticsService = StatisticsService(
            car_instance_list=car_instance_list, 
            driver_instance_list=driver_instance_list
        )

    # Drivers:

    def avrage_age(self):   
        avr_age = self.statisticsService.avreage_driver_age(force_int=True)
        
        if avr_age != 0:
            olt.show(
                title="Avrage driver age",
                message=f"The avrage driver age is {avr_age}"
            )
        else:
            olt.show(
                title="Error",
                message=f"No drivers saved"
            )

    def oldest_youngest_driver(self):
        drivers = self.statisticsService.oldest_youngest_driver()
        
        if drivers[0][1] != 0:
            olt.show(
                title="Oldest and youngest driver",
                message=f"The oldest driver is {drivers[0][0]} at {drivers[0][1]} years old, and"\
                        f"\nThe youngest driver is {drivers[1][0]} at {drivers[1][1]} years old"
            )
        else:
            olt.show(
                title="Error",
                message=f"No drivers saved"
            )
    
    def drivers_with_no_cars(self):
        drivers = ""
        for driver in self.statisticsService.drivers_with_no_cars():
            drivers += f"{driver}, "

        message = f"The drivers that do not have a car associated are {drivers}" \
                  if drivers is not "" \
                  else "All drivers have a car associated-"
        
        olt.show(
            title="Drivers with no cars",
            message=message[:-2]
        )

    
    # Cars:

    def cars_with_no_drivers(self):
        cars_ = self.statisticsService.cars_with_no_drivers()
        if cars_ != {}:
            table_contents = [["Car brand", "Car registration"]]
            for car_brand in cars_:
                table_contents.append([car_brand, cars_[car_brand]])
            
            table = SingleTable(table_contents, title="Cars with no driver associated")
            table.justify_columns = {
                    0: "center",
                    1: "center",
            }

            while True:
                console.clear_console()
                print(table.table)
                input_ = input("Type b or back to go back > ")
                if input_ == "b" or input_ == "back":
                    break
                else:
                    continue
        else:
            olt.show(
                title="Cars with no driver associated",
                message="All cars have at least a driver associated"
            )

    def most_popular_brand(self):
        most_popular = self.statisticsService.most_popular_car_brand()
        
        if most_popular != ():
            olt.show(
                title="Most popular car brand",
                message=f"The most popular brand is {most_popular[0]} with {most_popular[1]} cars"
            )
        else:
            olt.show(
                title="Error",
                message="No cars saved!"
            )

    def avrage_hp(self):
        avr_hp = self.statisticsService.avrage_car_hp(force_int=True)

        if avr_hp != 0:
            olt.show(
                title="Avrage car horsepower",
                message=f"The avrage hp is {avr_hp}"
            )
        else:
            olt.show(
                title="Error",
                message="No cars saved!"
            )


    def avrage_kms(self):
        avr_kms = self.statisticsService.avrage_car_kms(force_int=True)

        if avr_kms != 0:
            olt.show(
                title="Avrage car kilometers",
                message=f"The avrage kms is {avr_kms}"
            )
        else:
            olt.show(
                title="Error",
                message="No cars saved!"
            )
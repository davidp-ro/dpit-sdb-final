from typing import List, Dict, Tuple

class StatisticsService:
    """
    Class for statistics

    Public methods:
        Avrage age of drivers
        Show drivers with no cars
        Show cars with no drivers
        Most popular car brand
        Avrage car kilometers
        Avrage car horsepower
        Go back to previous men
    """
    car_instance_list = []
    driver_instance_list = []
    
    def __init__(self, car_instance_list: list, driver_instance_list: list):
        """
        Constructor for StatisticsService.

        Args:
            car_instance_list (list): Car instance list.
            driver_instance_list (list): Driver instance list.
        """
        self.car_instance_list = car_instance_list
        self.driver_instance_list = driver_instance_list

    def avreage_driver_age(self, force_int: bool = False) -> float or int:
        """
        Get the avrage driver age

        Args:
            force_int (bool, optional): Cast the result to int. Defaults to False.

        Returns:
            float or int: avrage driver age
        """
        age_sum = 0
        driver_num = 0

        for driver in self.driver_instance_list:
            driver_num += 1
            age_sum += driver.age

        if not force_int:
            return (age_sum / driver_num)
        else:
            return int(age_sum / driver_num)

    def oldest_youngest_driver(self) -> Tuple[Tuple[str, int], Tuple[str, int]]:
        """
        Get the oldest and youngest driver's name and age

        Returns:
            Tuple[2x Tuple[str, int]]: Oldest driver's name and age and youngest driver's name and age
        """
        oldest = ("", 0)
        youngest = ("", 999)
        for driver in self.driver_instance_list:
            if driver.age > oldest[1]:
                oldest = (driver.name, driver.age)
            if driver.age < youngest[1]:
                youngest = (driver.name, driver.age)

        return (oldest, youngest)


    def drivers_with_no_cars(self) -> List[str]:
        """
        Get drivers with no car associated

        Returns:
            List[str]: List with driver names
        """
        drivers_ = []

        for driver in self.driver_instance_list:
            if driver.car is None:
                drivers_.append(driver.name)

        return drivers_

    def cars_with_no_drivers(self) -> Dict[str, str]:
        """
        Get cars that have no driver associatted

        Returns:
            Dict[str, str]: Dictionary containing the brand and reg no for each unused car
        """
        used_ids = {}
        cars_ = {}

        for driver in self.driver_instance_list:
            if driver.car is not None:
                used_ids[driver.car.id] = None

        for car in self.car_instance_list:
            if not car.id in used_ids:
                cars_[car.brand] = car.reg

        return cars_

    def most_popular_car_brand(self) -> Tuple[str, int]:
        """
        Get the most popular brand

        Returns:
            Tuple[str, int]: The brand and the number of cars with that brand
        """
        most_popular = ("", 0) # most_popular_brand, max_aparitions
        aparitions = {}

        for car in self.car_instance_list:
            try:
                aparitions[car.brand] += 1
            except KeyError:
                aparitions[car.brand] = 1
            if aparitions[car.brand] > most_popular[1]:
                most_popular = car.brand, aparitions[car.brand]

        return most_popular

    def avrage_car_hp(self, force_int: bool = False) -> float or int:
        """
        Get the avrage car horespower

        Args:
            force_int (bool, optional): Cast the result to int. Defaults to False.

        Returns:
            float or int: avrage car hp
        """
        hp_sum = 0
        car_num = 0

        for car in self.car_instance_list:
            car_num += 1
            hp_sum += car.hp

        if not force_int:
            return (hp_sum / car_num)
        else:
            return int(hp_sum / car_num)

    def avrage_car_kms(self, force_int: bool = False) -> float or int:
        """
        Get the avrage car horespower

        Args:
            force_int (bool, optional): Cast the result to int. Defaults to False.

        Returns:
            float or int: avrage car hp
        """
        kms_sum = 0
        car_num = 0

        for car in self.car_instance_list:
            car_num += 1
            kms_sum += car.kms

        if not force_int:
            return (kms_sum / car_num)
        else:
            return int(kms_sum / car_num)

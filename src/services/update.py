from terminaltables import SingleTable
from utils.input_checker import Parser
from repository.repo import Repo
from repository.save_data import save_data
import ui.console_utils as console
import ui.one_line_table as olt

def handle_update_driver(driver_repo: Repo, parser: Parser, car_repo: Repo):
    # Get driver id:
    got_id = False
    _, driver_list = driver_repo.get()

    while not got_id:
        id_ = input("Enter driver id (numeric) or leave blank to see the driver list > ")
        if id_ is "":
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
                    got_id = True
                    done_id = False
                    done_age = False

                    while not done_id:
                        new_id = input("If you want to change the ID enter it now, leave blank to skip > ")
                        if new_id is not "":
                            try:
                                new_id = int(new_id)
                                done_id = True
                            except ValueError:
                                console.clear_console()
                                olt.show(
                                    title="Info",
                                    message="Invalid ID! The ID Must be numeric",
                                    go_back=False
                                )
                        else:
                            new_id = None
                            done_id = True

                    new_name = input("If you want to change the Name enter it now, leave blank to skip > ")
                    if new_name is "":
                        new_name = None

                    while not done_age:
                        new_age = input("If you want to change the Age enter it now, leave blank to skip > ")
                        if new_age is not "":
                            try:
                                new_age = int(new_age)
                                done_age = True
                            except ValueError:
                                console.clear_console()
                                olt.show(
                                    title="Info",
                                    message="Invalid ID! The ID Must be numeric",
                                    go_back=False
                                )
                        else:
                            new_age = None
                            done_age = True

                    new_car_yn = input("Do you want to change the driver's car enter \"y\" to change and \"n\" to skip > ").strip().lower()
                    if ord(new_car_yn) is 121: # Ascii code for y, had weird bug using only 'y'
                        new_car_id = input("Enter the new car's ID, leave blank to see all cars > ")
                        if new_car_id is "":
                            _, car_list = car_repo.get()
                            if len(car_list) is 0 or car_list is None:
                                olt.show(
                                    title="Something went wrong",
                                    message="Either there are no cars at this moment or something else went wrong"
                                )
                            else:
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

                                new_car_id = input("Enter the new car's ID > ")

                                try:
                                    new_car_id = int(new_car_id)
                                    resp, car = car_repo.get(mode="single", entity_id=new_car_id)
                                    if resp is "found":
                                        new_car = car
                                    else:
                                        olt.show(
                                            title="Fail",
                                            message="The car coudn't be found, discarding car changes",
                                            go_back=False
                                        )
                                except ValueError:
                                    olt.show(
                                        title="Fail",
                                        message="The car's id must be numeric, discarding car changes",
                                        go_back=False
                                    )
                        else:
                            try:
                                new_car_id = int(new_car_id)
                                resp, car = car_repo.get(mode="single", entity_id=new_car_id)
                                if resp is "found":
                                    new_car = car
                                else:
                                    olt.show(
                                        title="Fail",
                                        message="The car coudn't be found, discarding car changes",
                                        go_back=False
                                    )
                            except ValueError:
                                olt.show(
                                    title="Fail",
                                    message="The car's id must be numeric, discarding car changes",
                                    go_back=False
                                )
                    else:
                        new_car = None

                    driver_repo.update(
                        type_of_entity="driver",
                        entity_id=id_,
                        id=new_id,
                        name=new_name,
                        age=new_age,
                        car=new_car
                    )
                    save_data(
                        mode="single", 
                        only="drivers", 
                        driver_instance_list=driver_list
                    )
                    olt.show(
                        title="Success",
                        message="The driver was updated succesfully"
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

def handle_update_car(car_repo: Repo, parser: Parser):
    # Get car id:
    got_id = False
    _, car_list = car_repo.get()

    while not got_id:
        id_ = input("Enter car id (numeric) or leave blank to see the car list > ")
        if id_ is "":
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
                    got_id = True
                    done_id = False
                    done_hp = False
                    done_kms = False

                    while not done_id:
                        new_id = input("If you want to change the ID enter it now, leave blank to skip > ")
                        if new_id is not "":
                            try:
                                new_id = int(new_id)
                                done_id = True
                            except ValueError:
                                console.clear_console()
                                olt.show(
                                    title="Info",
                                    message="Invalid ID! The ID Must be numeric",
                                    go_back=False
                                )
                        else:
                            new_id = None
                            done_id = True
                    new_reg = input("If you want to change the Registration No. enter it now, leave blank to skip > ")
                    if new_reg is "":
                        new_reg = None

                    new_brand = input("If you want to change the Brand enter it now, leave blank to skip > ")
                    if new_brand is "":
                        new_brand = None

                    while not done_hp:
                        new_hp = input("If you want to change the Horsepower enter it now, leave blank to skip > ")
                        if new_hp is not "":
                            try:
                                new_hp = int(new_hp)
                                done_hp = True
                            except ValueError:
                                console.clear_console()
                                olt.show(
                                    title="Info",
                                    message="Invalid HP! The Horespower be a numeric value",
                                    go_back=False
                                )
                        else:
                            new_hp = None
                            done_hp = True
                        
                    while not done_kms:
                        new_kms = input("If you want to change the KMs enter them now, leave blank to skip > ")
                        if new_kms is not "":
                            try:
                                new_kms = int(new_kms)
                                done_kms = True
                            except ValueError:
                                console.clear_console()
                                olt.show(
                                    title="Info",
                                    message="Invalid KM! The KMs Must be numeric",
                                    go_back=False
                                )
                        else:
                            new_kms = None
                            done_kms = True

                    # Actually update-ing:
                    car_repo.update(
                        type_of_entity="car",
                        entity_id=id_,
                        id=new_id,
                        reg=new_reg,
                        brand=new_brand,
                        hp=new_hp,
                        kms=new_kms
                    )
                    save_data(
                        mode="single", 
                        only="cars", 
                        car_instance_list=car_list
                    )
                    olt.show(
                        title="Success",
                        message="The car was updated succesfully"
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
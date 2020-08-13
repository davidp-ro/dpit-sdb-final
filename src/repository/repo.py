from typing import Tuple
from ui.console_messages import warning, fail


class Repo:
    """
    Main repository Class - Deals with CRUD Ops for the entities

    Args:
        instance_list (list): The instance list for the respectiv enitity

    Example:
        repo = Repo(car_instance_list)
    """
    def __init__(self, instance_list: list) -> None:
        self.instance_list = instance_list

    def get(self, mode: str = "all", entity_id: int = None) -> Tuple[str, list or object]:
        """
        Get one or all(default) instance(s)

        Args:
            mode (str, optional): "all", "single" or "last". Defaults to "all".
            entity_id (int, optional): If mode was "single" then provide the entities id. Defaults to None.

        Returns:
            tuple(
                "found"/"not_found"/"failed",
                list or object: List if mode was "all", Car/Driver if mode was "single"
            )
        """
        if mode == "all":
            return ("found", self.instance_list)
        elif mode == "single":
            if entity_id is not None:
                for instance in self.instance_list:
                    if instance.id == entity_id:
                        return ("found", instance)
                return ("not_found", None)
            else:
                warning("In single mode, entity_id must not be None")
                return ("failed", None)
        elif mode == "last":
            if len(self.instance_list) == 0:
                return ("not_found", None)
            return ("found", self.instance_list[-1])
        else:
            warning("Invalid mode! Available modes: \"all\"(default), \"single\" or \"last\"")
            return ("failed", None)


    def add(self, entity: object) -> Tuple[str, str]:
        """
        Add an entity

        Args:
            entity (Car/Driver): The entity itself

        Example:
            add(car_instance_list, Car(...)) will return:
                ("ok", "Added succesfully") If the entity was succesfully added
                ("warn", "This already exists") If the entity already exists
                ("fail", "Something went wrong") If something failed

        Returns:
            tuple: (response, message), ie: ("ok", "Added succesfully")
        """
        try:
            response, _ = self.get("single", entity.id)
            if response == "not_found":
                self.instance_list.append(entity)
                return ("ok", "Added succesfully")
            elif response == "found":
                return ("warn", "This already exists")
            else:
                fail("Fail in repo::get")
                return ("fail", "Something went wrong")
        except Exception as e:
            fail(e)
            return ("fail", "Something went wrong")


    def delete(self, entity_id: int) -> Tuple[str, str]:
        """
        Deletes an entity

        Args:
            entity (Car/Driver): The entity itself

        Example:
            delete(1) will return:
                ("ok", "Deleted succesfully") If the entity was succesfully deleted
                ("warn", "Not found, maybe already deleted") Self-explanatory
                ("fail", "Something went wrong") If something failed

        Returns:
            tuple: (response, message), ie: ("ok", "Deleted succesfully")
        """
        resp, entity = self.get(mode="single", entity_id=int(entity_id))
        if resp == "found":
            self.instance_list.remove(entity)
            return ("ok", "Deleted succesfully")
        else:
            return ("warn", "Not found, maybe already deleted")


    def update(self, type_of_entity: str, entity_id: int, **kwargs) -> Tuple[str, str]:
        """
        Update an entity

        Args:
            type_of_entity (str): "car" / "driver"
            old_entity_id (int): The id of the entity that will get updated
            kwargs: Properties to update for each entity

        Raises:
            AttributeError: if given argument is incorrect

        Returns:
            tuple: (response, message), ie: ("ok", "Updated succesfully")

        Example:
            update(
                type_of_entity="car",
                entity_id=2,
                brand="New brand",
                kms=123456
            ) -> Will update the id, brand and kms for the entity that *had* entity_id
        """
        if type_of_entity == "car":
            resp, entity = self.get(mode="single", entity_id=entity_id)
            if resp == "found":
                # Update each given (kwargs) property
                if "id" in kwargs and kwargs["id"] is not None:
                    entity.id = kwargs["id"]
                if "reg" in kwargs and kwargs["reg"] is not None:
                    entity.reg = kwargs["reg"]
                if "brand" in kwargs and kwargs["brand"] is not None:
                    entity.brand = kwargs["brand"]
                if "hp" in kwargs and kwargs["hp"] is not None:
                    entity.hp = kwargs["hp"]
                if "kms" in kwargs and kwargs["kms"] is not None:
                    entity.kms = kwargs["kms"]
                return ("ok", "Updated succesfully")
            else:
                return ("fail", "Not found")
        elif type_of_entity == "driver":
            resp, entity = self.get(mode="single", entity_id=entity_id)
            if resp == "found":
                # Update each given (kwargs) property
                if "id" in kwargs and kwargs["id"] is not None:
                    entity.id = kwargs["id"]
                if "name" in kwargs and kwargs["name"] is not None:
                    entity.name = kwargs["name"]
                if "age" in kwargs and kwargs["age"] is not None:
                    entity.age = kwargs["age"]
                if "car" in kwargs and kwargs["car"] is not None:
                    if kwargs["car"] == -1:
                        entity.car = None
                    else:
                        entity.car = kwargs["car"]
                return ("ok", "Updated succesfully")
            else:
                return ("fail", "Not found")
        else:
            raise AttributeError("Invalid entity type!")
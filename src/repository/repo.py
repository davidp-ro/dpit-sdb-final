from ui.console_messages import warning, fail


class Repo:
    instance_list = []
    
    def __init__(self, instance_list: list):
        self.instance_list = instance_list

    def get(self, mode: str = "all", entity_id: int = None) -> tuple:
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
        if mode is "all":
            return ("found", self.instance_list)
        elif mode is "single":
            if entity_id is not None:
                for instance in self.instance_list:
                    if instance.id is entity_id:
                        return ("found", instance)
                return ("not_found", None)
            else:
                warning("In single mode, entity_id must not be None")
                return ("failed", None)
        elif mode is "last":
            if len(self.instance_list) is 0:
                return ("not_found", None)
            return ("found", self.instance_list[-1])
        else:
            warning("Invalid mode! Available modes: \"all\"(default), \"single\" or \"last\"")
            return ("failed", None)


    def add(self, entity: object) -> tuple:
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
            if response is "not_found":
                self.instance_list.append(entity)
                return ("ok", "Added succesfully")
            elif response is "found":
                return ("warn", "This already exists")
            else:
                fail("Fail in repo::get")
                return ("fail", "Something went wrong")
        except Exception as e:
            fail(e)
            return ("fail", "Something went wrong")


    def delete(self, entity_id: int) -> tuple:
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
        if resp is "found":
            self.instance_list.remove(entity)
            return ("ok", "Deleted succesfully")
        else:
            return ("warn", "Not found, maybe already deleted")


    def update(self, type_of_entity: str, entity_id: int, **kwargs) -> tuple:
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
        if type_of_entity is "car":
            resp, entity = self.get(mode="single", entity_id=entity_id)
            if resp is "found":
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
        elif type_of_entity is "driver":
            resp, entity = self.get(mode="single", entity_id=entity_id)
            if resp is "found":
                # Update each given (kwargs) property
                if "id" in kwargs and kwargs["id"] is not None:
                    entity.id = kwargs["id"]
                if "name" in kwargs and kwargs["name"] is not None:
                    entity.name = kwargs["name"]
                if "age" in kwargs and kwargs["age"] is not None:
                    entity.age = kwargs["age"]
                if "car" in kwargs and kwargs["car"] is not None:
                    entity.car = kwargs["car"]
                return ("ok", "Updated succesfully")
            else:
                return ("fail", "Not found")
        else:
            raise AttributeError("Invalid entity type!")
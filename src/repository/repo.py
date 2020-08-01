from ui.console_messages import warning, fail

def get(
    instance_list: list, 
    mode: str = "single", 
    entity_id: int = None) -> tuple(str, list or object):
    """
    Get one(default) or all instance(s)

    Args:
        instance_list (list): The instance list
        mode (str, optional): "all" or "single". Defaults to "single".
        entity_id (int, optional): If mode was "single" then provide the entities id. Defaults to None.

    Returns:
        tuple(
            "found"/"not_found"/"failed",
            list or object: List if mode was "all", Car/Driver if mode was "single"
        )
    """
    if mode is "all":
        return ("found", instance_list)
    elif mode is "single":
        if entity_id is not None:
            for instance in instance_list:
                if instance.id is entity_id:
                    return ("found", instance)
            return ("not_found", None)
        else:
            warning("In single mode, entity_id must not be None")
            return ("failed", None)           
    else:
        warning("Invalid mode! Available modes: \"all\"(default) or \"single\"")
        return ("failed", None)


def add(instance_list: list, entity: object) -> tuple:
    """
    Add an entity to it's respective list

    Args:
        instance_list (list): The list that contains instances of the entity
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
        response, _ = get(instance_list, "single", entity.id)
        if response is "not_found":
            instance_list.append(entity)
            return ("ok", "Added succesfully")
        elif response is "found":
            return ("warn", "This already exists")
        else:
            fail("Fail in repo::get")
            return ("fail", "Something went wrong")
    except Exception as e:
        fail(e)
        return ("fail", "Something went wrong")


def delete(instance_list: list, entity: object) -> tuple:
    """
    Deletes an entity from it's respective list

    Args:
        instance_list (list): The list that contains instances of the entity
        entity (Car/Driver): The entity itself

    Example:
        delete(car_instance_list, Car(...)) will return:
            ("ok", "Deleted succesfully") If the entity was succesfully deleted
            ("warn", "This was already deleted") If the entity was already deleted
            ("fail", "Something went wrong") If something failed

    Returns:
        tuple: (response, message), ie: ("ok", "Deleted succesfully")
    """
    pass


def update(instance_list: list, old_entity_id: int, new_entity: object) -> tuple:
    """
    Update an entity from it's respective list

    Args:
        instance_list (list): The list that contains instances of the entity
        old_entity_id (int): The entity that gets updated's id
        new_entity (Car/Driver): The updated entity

    Example:
        update(car_instance_list, 1, Car(...)) will return:
            ("ok", "Updated succesfully") If the entity was succesfully added
            ("fail", "Initial instance not found") If old_entity dosen't exist
            ("fail", "Something went wrong") If something failed

    Returns:
        tuple: (response, message), ie: ("ok", "Added succesfully")
    """
    pass
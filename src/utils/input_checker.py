from repository.repo import Repo
from ui.console_messages import fail
from models.car import Car
from models.driver import Driver

class Parser:
    entity_repository = None

    def __init__(self, entity_repository: Repo):
        self.entity_repository = entity_repository

    def check_if_already_exists(self, by_id: bool = False, id: int = None, name_or_reg: str = None) -> bool or None:
        """
        Checks if a entity exists

        Args:
            by_id (bool, optional): True check by ID, false check by name/reg. Defaults to False.
            id (int, optional): ID (if used). Defaults to None.
            name_or_reg (str, optional): Driver name or Car reg (if used). Defaults to None.

        Returns:
            bool: True if already exists, False if it doesn't
            or None if something fails
        """
        if by_id:
            if id is not None:
                response, _ = self.entity_repository.get("single", id)
                if response is "found":
                    return True
                elif response is "not_found":
                    return False
                else:
                    fail("entity_repository.get FAILED in utils::input_checker")
                    return None
            else:
                fail("ID Must not be None in utils::input_checker")
                return None
        else:
            if name_or_reg is not None:
                response, entity_list = self.entity_repository.get()
                if isinstance(entity_list[0], Driver):
                    # Drivers so check with name
                    for entity in entity_list:
                        if entity.name is name_or_reg:
                            return True
                    return False
                else:
                    # Cars so check with regs
                    for entity in entity_list:
                        if entity.reg is name_or_reg:
                            return True
                    return False
            else:
                fail("name_or_reg Must not be None in utils::input_checker")
                return None

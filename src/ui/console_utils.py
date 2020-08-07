import os
import platform


def clear_console() -> None:
    """
    Checks the platform and issues the right command to clear the console
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
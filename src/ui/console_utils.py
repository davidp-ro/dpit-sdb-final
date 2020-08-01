import os
import platform


def clear_console():
    if platform.system() is "Windows":
        os.system("cls")
    else:
        os.system("clear")
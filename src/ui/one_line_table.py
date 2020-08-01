from terminaltables import SingleTable
import ui.console_utils as console

def show(title: str, message: str) -> None:
    """
    Show a table, useful for short pages

    Args:
        title (str): Table title    
        message (str): Table content
    """
    while True:
        about_message = [[message]]
        about_page = SingleTable(about_message, title="About")
        console.clear_console()
        print(about_page.table)
        input_ = input("Type b or back to go back > ")
        if input_ == "b" or input_ == "back":
            break
        else:
            continue
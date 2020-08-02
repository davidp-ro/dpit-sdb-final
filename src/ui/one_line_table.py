from terminaltables import SingleTable
import ui.console_utils as console

def show(title: str, message: str, go_back: bool = True) -> None:
    """
    Show a table, useful for short pages

    Args:
        title (str): Table title 
        message (str): Table content
        go_back (bool, optional): If false will not show go back prompt. Defaults to True.
    """
    if go_back:
        while True:
            table_message = [[message]]
            table = SingleTable(table_message, title=title)
            console.clear_console()
            print(table.table)
            input_ = input("Type b or back to go back > ")
            if input_ == "b" or input_ == "back":
                break
            else:
                continue
    else:
        table_message = [[message]]
        table = SingleTable(table_message, title=title)
        console.clear_console()
        print(table.table)

class Menu:
    DISPLAY_ALL_BOOKS = "Display all Books"
    SEARCH_BOOKS = "Search Book"
    BORROW_A_BOOK = "Borrow a Book"
    CART = "Cart"
    BORROWED_BOOKS = "Borrowed Books"
    EXIT = "Exit"
    OPEN_LIBRARY = "Open the library"
    CLOSE_LIBRARY = "Close the library "
    HELP = "Show Menu Options"

    menu = {
        1: OPEN_LIBRARY,
        2: CLOSE_LIBRARY,
        3: DISPLAY_ALL_BOOKS,
        4: SEARCH_BOOKS,
        5: BORROW_A_BOOK,
        6: CART,
        7: BORROWED_BOOKS,
        8: EXIT,
        9: HELP
    }

    @staticmethod
    def print_menu() -> None:
        longest_desc = max([len(desc) for desc in Menu.menu.values()])
        dashes = '-' * (longest_desc + 11)
        print(dashes)
        for key in Menu.menu:
            spaces = ' ' * (longest_desc - len(Menu.menu[key]))
            print(f"|   {key} - {Menu.menu[key] + spaces}   |")
        print(dashes)

    @staticmethod
    def get_menu_keys() -> list:
        return list(Menu.menu.keys())

    @staticmethod
    def ask_for_menu_option() -> int:
        while True:
            # ask for user input
            selection = input("Please select Menu option ")
            # check user input is a number (when not valid continue to next iteration)
            if not selection.isnumeric():
                print(f"Selection must be a number {Menu.get_menu_keys()}")
                continue
            # check user input is in the menu (when not valid continue to next iteration)
            selection = int(selection)
            if selection not in Menu.menu:
                print(f"Selection must be a valid option {Menu.get_menu_keys()}")
                continue

            # return a valid option
            return selection


# Marco Stevanella - 101307949

# IMPORTS
from menu import Menu
from library import Library, SearchBy

# Create the library OBJ
library = Library()
# PRINT MENU
Menu.print_menu()
while True:
    user_input = Menu.ask_for_menu_option()
    # DISPLAY BOOKS IN LIBRARY
    if Menu.menu[user_input] == Menu.OPEN_LIBRARY:
        library.open_library()
        library.seed_library()
    elif Menu.menu[user_input] == Menu.CLOSE_LIBRARY:
        library.close_library()
    if Menu.menu[user_input] == Menu.DISPLAY_ALL_BOOKS:
        library.display_books()
    # SEARCH A BOOK IN LIBRARY BY CATEGORY
    elif Menu.menu[user_input] == Menu.SEARCH_BOOKS:
        category = input('Which Category would you like to search the book by? ')
        # todo: fix enum
        if category in [key.value for key in SearchBy]:
            query_value = input(f'Input the {category} you want to find : ')
            # pass key and value to search_by method
            library.search_by(category, query_value)
        else:
            print(f'We can only search by  {SearchBy.TITLE.value}, {SearchBy.AUTHOR.value} or {SearchBy.GENRE.value}')
    elif Menu.menu[user_input] == Menu.BORROW_A_BOOK:
        # find the book and insert a new record to the cart table
        library.display_books()
        selected_id = int(input("Could you tell me the ID of the book you want to borrow?"))
        borrowed_book = library.select_book(selected_id)
        library.borrow(borrowed_book.book_id)
        pass
    elif Menu.menu[user_input] == Menu.CART:
        # display the user what's in the cart
        #   inner join table books and cart to display books in the cart
        library.display_books_in_cart()
        # ask the user if she wants to borrow the books in the cart
        while True:
            answer = input("Would you like to borrow the books? 'y' for yes 'n' for no ")
            if answer == 'y' or answer == 'Y':
                library.print_total_amount()
            else:
                break
            answer = input("Would you like to pay? 'y' for yes 'n' for no ")
            if answer == 'y' or answer == 'Y':
                # delete book from cart table and set them in new borrowed books table
                # if yes print a recept with the total amount due and ask if it is ok to proceed with payment.
                library.process_books_from_cart_to_borrow()
                break
            else:
                break
                # if no return to menu
    elif Menu.menu[user_input] == Menu.BORROWED_BOOKS:
        library.display_borrowed_books()
    elif Menu.menu[user_input] == Menu.EXIT:
        break
    elif Menu.menu[user_input] == Menu.HELP:
        Menu.print_menu()
print("Goodbye!")

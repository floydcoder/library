from __future__ import annotations
from book import Book
from enum import Enum
from DB.db import DB
from file_manager import FileManager


class SearchBy(Enum):
    TITLE = 'title'
    AUTHOR = 'author'
    GENRE = 'genre'


class Library:

    def __init__(self,):
        self.books = []
        self.selected_books = []

    def stock_books(self, new_books: list[Book]):
        self.books.extend(new_books)

    def search_by(self, search_key: str, search_val: str):
        books = DB.query_by_category(search_key, search_val)
        for book in books:
            print(book)

    def select_book(self, book_id: int):
        books = DB.find_book_by_id(book_id)
        for book in books:
            print(f"The book {book.title} - {book.author} published it in {book.year} is in your cart!")
            return book

    def borrow(self, book_id: int):
        DB.update_borrowing_status(book_id)
        DB.insert_borrowed_book_in_cart(book_id)
        # Create/display receipt
        pass

    def display_books(self):
        books = DB.retrieve_all_books()
        for book in books:
            print(book)

    def open_library(self):
        DB.init_tables()

    def seed_library(self):
        books = FileManager.read_csv_file("csv/books.csv")
        DB.insert_books_to_db(books)

    def close_library(self):
        DB.drop_tables()

    @staticmethod
    def display_books_in_cart():
        books = DB.retrieve_books_in_cart()
        for book in books:
            print(book)

    @staticmethod
    def print_total_amount():
        books = DB.retrieve_books_in_cart()
        total_amount = 0.00
        for book in books:
            total_amount += book.borrowing_fee
        print(f"Your total amount is: {round(total_amount, 2)}")

    @staticmethod
    def process_books_from_cart_to_borrow():
        DB.move_books_from_cart_to_borrowed()
        print("Thank you for using the Library, don't forget to return the books!")

    @staticmethod
    def display_borrowed_books():
        books = DB.display_borrowed_books()
        for book in books:
            print(book.__str__())



from __future__ import annotations


class Book:
    HEADERS = {
        'BOOK_ID': "Book ID",
        'TITLE': "Title",
        'AUTHOR': "Author",
        'GENRE': "Genre",
        'YEAR': "Year",
        'ISBN': "ISBN",
        'IS_AVAILABLE': "Availability",
        'BORROWING_FEE': "Borrowing fee",
        'BORROWING_DAYS': "Borrowing days"
    }

    def __init__(self, book_id: int, title: str, author: str, genre: str, year: int, isbn: int, is_borrowed: int,
                 borrowing_fee: float, borrowing_days: int):

        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.genre: str = genre
        self.year: int = year
        self.isbn: int = isbn
        self.is_borrowed: int = is_borrowed
        self.borrowing_fee: float = borrowing_fee
        self.borrowing_days: int = borrowing_days

    def __str__(self):
        return f"ID: {self.book_id}" \
               f" TITLE: {self.title}" \
               f" AUTHOR: {self.author}" \
               f" GENRE: {self.genre}" \
               f" YEAR: {self.year}" \
               f" ISBN: {self.isbn}" \
               f" BORROWED: {self.is_borrowed}" \
               f" BORROWING FEE: {self.borrowing_fee}" \
               f" BORROWING DAYS: {self.borrowing_days} "

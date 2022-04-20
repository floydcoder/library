from __future__ import annotations
import csv
from book import Book


class FileManager:
    @staticmethod
    def read_csv_file(filename: str) -> list[Book]:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            books = []
            for row in reader:
                book = Book(
                    book_id=int(row['book_id']),
                    title=row['title'],
                    author=row['author'],
                    genre=row['genre'],
                    year=int(row['year']),
                    isbn=int(row['isbn']),
                    is_borrowed=int(row['is_borrowed']),
                    borrowing_fee=float(row['borrowing_fee']),
                    borrowing_days=int(row['borrowing_days'])
                )
                books.append(book)
            return books


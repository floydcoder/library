from __future__ import annotations
import sqlite3
import datetime
from typing import List
from book import Book
from borrowed import Borrowed


class DB:
    @staticmethod
    def create_book_table():
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = '''create table book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL CHECK(title != ''),
                author TEXT NOT NULL CHECK(author != ''),
                genre TEXT NOT NULL CHECK(genre != ''),
                year INTEGER NOT NULL,
                isbn INTEGER UNIQUE CHECK (length(isbn) >= 13),
                is_borrowed INTEGER CHECK(is_borrowed >= 0 AND is_borrowed <= 1),
                borrowing_fee REAL NOT NULL CHECK(borrowing_fee > 0),
                borrowing_days INTEGER NOT NULL CHECK(borrowing_days > 0)
            )'''
            c.execute(query)
            conn.close()
        except Exception as e:
            print("The table book is already present in the database")

    @staticmethod
    def create_cart_table():
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = '''create table cart (
                    id INTEGER NOT NULL,
                    FOREIGN KEY(id) REFERENCES book(id)
                )'''
            c.execute(query)
            conn.close()
        except Exception as e:
            print("The table Cart is already present in the database")

    @staticmethod
    def create_borrowed_table():
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = '''create table borrowed (
                        id INTEGER NOT NULL,
                        returnBy TEXT NOT NULL CHECK(returnBy != ''),
                        FOREIGN KEY(id) REFERENCES book(id)
                    )'''
            c.execute(query)
            conn.close()
        except Exception as e:
            print("The table Cart is already present in the database")

    @staticmethod
    def query_by_category(col: str, val: str) -> list[Book]:
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = f"""select * from book where {col}='{val}'"""
            c.execute(query)
            rows = c.fetchall()
            conn.close()
            books = []
            for row in rows:
                book_id, title, author, genre, year, isbn, is_borrowed, borrowing_fee, borrowing_days = row
                book = Book(
                    book_id=book_id,
                    title=title,
                    author=author,
                    genre=genre,
                    year=year,
                    isbn=isbn,
                    is_borrowed=is_borrowed,
                    borrowing_fee=borrowing_fee,
                    borrowing_days=borrowing_days
                )
                books.append(book)
            return books
        except Exception as e:
            print("Sorry, we don't have that book in the library")

    @staticmethod
    def retrieve_all_books() -> list[Book]:
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = '''select * from book'''
            c.execute(query)
            rows = c.fetchall()
            conn.close()
            books = []
            for row in rows:
                book_id, title, author, genre, year, isbn, is_borrowed, borrowing_fee, borrowing_days = row
                book = Book(
                    book_id=book_id,
                    title=title,
                    author=author,
                    genre=genre,
                    year=year,
                    isbn=isbn,
                    is_borrowed=is_borrowed,
                    borrowing_fee=borrowing_fee,
                    borrowing_days=borrowing_days
                )
                books.append(book)
            return books
        except Exception as e:
            print("The library is currently closed, open it first!")

    @staticmethod
    def insert_books_to_db(books: List[Book]):
        try:
            conn = sqlite3.Connection('DB/library.sqlite')
            c = conn.cursor()
            for book in books:
                sql = '''INSERT INTO book(
                title,
                author,
                genre,
                year,
                isbn,
                is_borrowed,
                borrowing_fee,
                borrowing_days) VALUES 
                (?,?,?,?,?,?,?,?)'''
                c.execute(sql, (book.title,
                                book.author,
                                book.genre,
                                book.year,
                                book.isbn,
                                book.is_borrowed,
                                book.borrowing_fee,
                                book.borrowing_days))
                conn.commit()
            conn.close()
            print("the library is now open!")
        except Exception as e:
            print("Search for a book to borrow!")

    @staticmethod
    def init_tables():
        # create table
        DB.create_book_table()
        DB.create_cart_table()
        DB.create_borrowed_table()


    @staticmethod
    def drop_tables():
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = '''
                DROP TABLE IF EXISTS cart;
                DROP TABLE IF EXISTS book;
                DROP TABLE IF EXISTS borrowed;
            '''
            books = c.executescript(query)
            conn.close()
            print("We have closed the library, bye bye")
        except Exception as e:
            print("We could not close the Library, some people are still inside")

    @staticmethod
    def find_book_by_id(book_id: int):
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = f"""select * from book where id== {book_id}"""
            c.execute(query)
            rows = c.fetchall()
            conn.close()
            books = []
            for row in rows:
                book_id, title, author, genre, year, isbn, is_borrowed, borrowing_fee, borrowing_days = row
                book = Book(
                    book_id=book_id,
                    title=title,
                    author=author,
                    genre=genre,
                    year=year,
                    isbn=isbn,
                    is_borrowed=is_borrowed,
                    borrowing_fee=borrowing_fee,
                    borrowing_days=borrowing_days
                )
                books.append(book)
            return books
        except Exception as e:
            print("I am sorry, we didn't a book with that ID, try again...")

    @staticmethod
    def update_borrowing_status(book_id: int):
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = f"""UPDATE book SET is_borrowed = 1 WHERE id = {book_id} """
            c.execute(query)
            conn.close()
        except Exception as e:
            print("Somehow we could not update the status of the book")

    @staticmethod
    def insert_borrowed_book_in_cart(book_id: int):
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = f"""INSERT INTO cart(id) VALUES ({book_id})"""
            c.execute(query)
            conn.commit()
            conn.close()
        except Exception as e:
            print("Somehow we could not insert your book to the cart")

    @staticmethod
    def retrieve_books_in_cart():
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            query = f""" SELECT book.id,
                                book.title,
                                book.author,
                                book.genre,
                                book.year,
                                book.isbn,
                                book.is_borrowed,
                                book.borrowing_fee,
                                book.borrowing_days
                            FROM book
                            INNER JOIN cart ON book.id = cart.id """
            c.execute(query)
            rows = c.fetchall()
            conn.close()
            books = []
            for row in rows:
                book_id, title, author, genre, year, isbn, is_borrowed, borrowing_fee, borrowing_days = row
                book = Book(
                    book_id=book_id,
                    title=title,
                    author=author,
                    genre=genre,
                    year=year,
                    isbn=isbn,
                    is_borrowed=is_borrowed,
                    borrowing_fee=borrowing_fee,
                    borrowing_days=borrowing_days
                )
                books.append(book)
            return books
        except Exception as e:
            print("It seems like someone already borrowed these books while you were away")
    @staticmethod
    def calculate_return_date(days: int) -> str:
        starting_date = str(datetime.date.today().strftime("%m-%d-%y"))
        #dd-mm-yy
        today = datetime.datetime.strptime(starting_date, "%m-%d-%y")
        return_date = today + datetime.timedelta(days=4)
        return str(return_date)

    @staticmethod
    def move_books_from_cart_to_borrowed():
        try:
            conn = sqlite3.connect('DB/library.sqlite')
            c = conn.cursor()
            books = DB.retrieve_books_in_cart()
            # copies the ids to the borrowed table
            for book in books:
                return_date = DB.calculate_return_date(book.borrowing_days)
                query = f"""INSERT INTO borrowed(id, returnBy) VALUES (?,?) """
                c.execute(query, (book.book_id, return_date))
                conn.commit()
            # delete all records from cart, since it has been checked out
            # query = f"""DELETE FROM cart WHERE cart.id IN (
            # SELECT cart.id FROM cart i INNER JOIN borrowed b ON (i.id = b.id));
            #  """
            # query = """DELETE FROM cart WHERE cart.id IN (
            # SELECT cart.id FROM cart i INNER JOIN borrowed b on i.id = b.id);
            #  """
            query = """DELETE FROM cart"""
            c.execute(query)
            conn.commit()
            conn.close()
        except Exception as e:
            print("Something went wrong while moving the books from the cart to the table")

    @staticmethod
    def display_borrowed_books():
        conn = sqlite3.connect('DB/library.sqlite')
        c = conn.cursor()
        return_books = []
        query = """ SELECT  
                            brw.id,
                            bk.id,
                            bk.title,
                            bk.author,
                            bk.genre,
                            bk.year,
                            bk.isbn,
                            bk.is_borrowed,
                            bk.borrowing_fee,
                            bk.borrowing_days,
                            brw.returnBy
                        FROM borrowed brw
                        LEFT JOIN book bk USING(id)
            """
        c.execute(query)
        rows = c.fetchall()
        conn.close()
        borrowed_books = []
        for row in rows:
            borrowed_id, book_id, title, author, genre, year, isbn, is_borrowed, borrowing_fee, borrowing_days, return_date = row
            book = Borrowed(
                book_id=book_id,
                title=title,
                author=author,
                genre=genre,
                year=year,
                isbn=isbn,
                is_borrowed=is_borrowed,
                borrowing_fee=borrowing_fee,
                borrowing_days=borrowing_days,
                borrowed_id=borrowed_id,
                return_date=return_date
            )
            borrowed_books.append(book)
        return borrowed_books












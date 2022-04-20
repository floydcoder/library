from book import Book


class Borrowed(Book):
    def __init__(self, book_id: int, title: str, author: str, genre: str, year: int, isbn: int, is_borrowed: int,
                 borrowing_fee: float, borrowing_days: int, borrowed_id: int, return_date: str):
        super().__init__(book_id, title, author, genre, year, isbn, is_borrowed, borrowing_fee, borrowing_days)
        self.borrowed_id = int(borrowed_id)
        self.return_date = str(return_date)

    def __str__(self) -> str:
        return f"book id: {self.book_id} return date: {self.return_date.split(' ')[0]}"





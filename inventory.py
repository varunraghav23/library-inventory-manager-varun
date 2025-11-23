import logging

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Added book: {book.title}")

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.status == "available":
                book.status = "issued"
                logging.info(f"Issued book: {book.title}")
                return True
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.status == "issued":
                book.status = "available"
                logging.info(f"Returned book: {book.title}")
                return True
        return False

    def view_all(self):
        return self.books

    def search(self, keyword):
        return [
            book for book in self.books
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()
        ]

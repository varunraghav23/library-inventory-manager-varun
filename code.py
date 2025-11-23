import logging

# ---------------- Logging Configuration ----------------
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------- Book Class -----------------------
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {self.status}")

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            logging.info(f"Book issued: {self.title} ({self.isbn})")
            print("Book issued successfully.")
        else:
            logging.error(f"Issue failed! Book already issued: {self.title} ({self.isbn})")
            print("Book is already issued.")

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            logging.info(f"Book returned: {self.title} ({self.isbn})")
            print("Book returned successfully.")
        else:
            logging.error(f"Return failed! Book not issued: {self.title} ({self.isbn})")
            print("Book was not issued.")


# ---------------- LibraryInventory Class ----------------
class LibraryInventory:
    def __init__(self):
        self.books = []
        logging.info("Library Inventory started.")

    def add_book(self, title, author, isbn):
        try:
            book = Book(title, author, isbn)
            self.books.append(book)
            logging.info(f"Book added: {title}, {author}, {isbn}")
            return book
        except Exception as e:
            logging.error(f"Error adding book: {e}")
            raise ValueError("Failed to add book")

    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book:
            book.issue()
            return True
        else:
            logging.error(f"Issue failed. Book not found: {isbn}")
            return False

    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book:
            book.return_book()
            return True
        else:
            logging.error(f"Return failed. Book not found: {isbn}")
            return False

    def search_by_title(self, title):
        results = [b for b in self.books if title.lower() in b.title.lower()]
        logging.info(f"Searched by title: '{title}' found {len(results)} results")
        return results

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                logging.info(f"Book found by ISBN: {isbn}")
                return b
        logging.warning(f"No book found for ISBN: {isbn}")
        return None

    def display_all(self):
        if not self.books:
            logging.warning("Display failed: No books in inventory")
            print("No books in inventory.")
        else:
            logging.info("Displayed all books.")
            print("\nAll Books:")
            for b in self.books:
                print(b)

    def save_to_file(self):
        try:
            with open("library.txt", "w") as f:
                for b in self.books:
                    f.write(f"{b.title},{b.author},{b.isbn},{b.status}\n")
            logging.info("Library saved to file.")
        except Exception as e:
            logging.error(f"Error saving to file: {e}")


# ---------------------- MENU ---------------------------
def menu():
    inv = LibraryInventory()

    while True:
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search by Title")
        print("6. Search by ISBN")
        print("7. Save to File")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                t = input("Title: ")
                a = input("Author: ")
                i = input("ISBN: ")
                book = inv.add_book(t, a, i)
                print("Added:", book)

            elif choice == "2":
                i = input("ISBN: ")
                print("Issued." if inv.issue_book(i) else "Cannot issue.")

            elif choice == "3":
                i = input("ISBN: ")
                print("Returned." if inv.return_book(i) else "Cannot return.")

            elif choice == "4":
                inv.display_all()

            elif choice == "5":
                q = input("Title query: ")
                res = inv.search_by_title(q)
                print("\n".join(str(b) for b in res) if res else "No matches.")

            elif choice == "6":
                i = input("ISBN: ")
                b = inv.search_by_isbn(i)
                print(b if b else "Not found.")

            elif choice == "7":
                inv.save_to_file()
                print("Saved to file.")

            elif choice == "0":
                logging.info("Program exited by user.")
                print("Exiting...")
                break

            else:
                logging.warning("Invalid menu choice entered.")
                print("Invalid choice.")

        except Exception as e:
            logging.error(f"Unexpected error in menu: {e}")
            print("An error occurred. Check logs.")


# To start the program:
 menu()

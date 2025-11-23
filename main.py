from library_manager import Book, LibraryInventory

def menu():
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

inventory = LibraryInventory()

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book Added!")

        elif choice == "2":
            isbn = input("Enter ISBN to Issue: ")
            print("Issued!" if inventory.issue_book(isbn) else "Book not available.")

        elif choice == "3":
            isbn = input("Enter ISBN to Return: ")
            print("Returned!" if inventory.return_book(isbn) else "Invalid return.")

        elif choice == "4":
            for book in inventory.view_all():
                print(book)

        elif choice == "5":
            keyword = input("Enter title/author: ")
            results = inventory.search(keyword)
            if results:
                for book in results:
                    print(book)
            else:
                print("No matches found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

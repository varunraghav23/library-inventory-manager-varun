import pytest
from library_manager import LibraryInventory, Book

def test_add_book():
    inv = LibraryInventory()
    b = Book("Test", "Author", "123")
    inv.add_book(b)
    assert len(inv.books) == 1

def test_issue_book():
    inv = LibraryInventory()
    b = Book("Test", "Author", "123")
    inv.add_book(b)
    assert inv.issue_book("123") is True
    assert b.status == "issued"

def test_return_book():
    inv = LibraryInventory()
    b = Book("Test", "Author", "123", status="issued")
    inv.add_book(b)
    assert inv.return_book("123") is True
    assert b.status == "available"

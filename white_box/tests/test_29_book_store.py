"""
Unit tests for book_store.
"""

import unittest
from unittest.mock import patch

from white_box.book_store import Book, BookStore


class TestBook(unittest.TestCase):
    """
    Tests for Book class.
    """

    def test_constructor_saves_values(self):
        """
        Verifies that constructor assigns all attributes correctly.
        """
        book = Book("Clean Code", "Robert C. Martin", 25.5, 8)

        self.assertEqual("Clean Code", book.title)
        self.assertEqual("Robert C. Martin", book.author)
        self.assertEqual(25.5, book.price)
        self.assertEqual(8, book.quantity)

    @patch("builtins.print")
    def test_display_prints_expected_lines_in_order(self, mocked_print):
        """
        Verifies the printed output of display().
        """
        book = Book("Dune", "Frank Herbert", 30, 4)

        book.display()

        expected_calls = [
            unittest.mock.call("Title: Dune"),
            unittest.mock.call("Author: Frank Herbert"),
            unittest.mock.call("Price: $30"),
            unittest.mock.call("Quantity: 4"),
        ]
        mocked_print.assert_has_calls(expected_calls)
        self.assertEqual(4, mocked_print.call_count)


class TestBookStore(unittest.TestCase):
    """
    Tests for BookStore class.
    """

    def setUp(self):
        """
        Creates a store and sample books.
        """
        self.store = BookStore()
        self.book_a = Book("Python 101", "Mike", 15.0, 2)
        self.book_b = Book("Java Basics", "Ana", 20.0, 5)
        self.book_c = Book("Python 101", "Laura", 18.0, 1)

    def test_store_starts_empty(self):
        """
        Verifies bookstore starts with no books.
        """
        self.assertListEqual([], self.store.books)

    @patch("builtins.print")
    def test_add_book_appends_book_and_prints_message(self, mocked_print):
        """
        Verifies add_book stores the book and prints confirmation.
        """
        self.store.add_book(self.book_a)

        self.assertEqual(1, len(self.store.books))
        self.assertIs(self.book_a, self.store.books[0])
        mocked_print.assert_called_once_with("Book 'Python 101' added to the store.")

    @patch("builtins.print")
    def test_display_books_when_store_is_empty(self, mocked_print):
        """
        Verifies the message shown when there are no books.
        """
        self.store.display_books()

        mocked_print.assert_called_once_with("No books in the store.")

    @patch("builtins.print")
    def test_display_books_when_store_has_items(self, mocked_print):
        """
        Verifies store listing with multiple books.
        """
        self.store.books = [self.book_a, self.book_b]

        self.store.display_books()

        expected_calls = [
            unittest.mock.call("Books available in the store:"),
            unittest.mock.call("Title: Python 101"),
            unittest.mock.call("Author: Mike"),
            unittest.mock.call("Price: $15.0"),
            unittest.mock.call("Quantity: 2"),
            unittest.mock.call("Title: Java Basics"),
            unittest.mock.call("Author: Ana"),
            unittest.mock.call("Price: $20.0"),
            unittest.mock.call("Quantity: 5"),
        ]
        mocked_print.assert_has_calls(expected_calls)
        self.assertEqual(9, mocked_print.call_count)

    @patch("builtins.print")
    def test_search_book_returns_message_when_title_not_found(self, mocked_print):
        """
        Verifies search output when no title matches.
        """
        self.store.books = [self.book_a, self.book_b]

        self.store.search_book("Unknown Title")

        mocked_print.assert_called_once_with(
            "No book found with title 'Unknown Title'."
        )

    @patch("builtins.print")
    def test_search_book_finds_one_match(self, mocked_print):
        """
        Verifies search output for a single matching book.
        """
        self.store.books = [self.book_a, self.book_b]

        self.store.search_book("Python 101")

        expected_calls = [
            unittest.mock.call("Found 1 book(s) with title 'Python 101':"),
            unittest.mock.call("Title: Python 101"),
            unittest.mock.call("Author: Mike"),
            unittest.mock.call("Price: $15.0"),
            unittest.mock.call("Quantity: 2"),
        ]
        mocked_print.assert_has_calls(expected_calls)
        self.assertEqual(5, mocked_print.call_count)

    @patch("builtins.print")
    def test_search_book_is_case_insensitive(self, mocked_print):
        """
        Verifies search ignores letter case.
        """
        self.store.books = [self.book_a]

        self.store.search_book("python 101")

        expected_calls = [
            unittest.mock.call("Found 1 book(s) with title 'python 101':"),
            unittest.mock.call("Title: Python 101"),
            unittest.mock.call("Author: Mike"),
            unittest.mock.call("Price: $15.0"),
            unittest.mock.call("Quantity: 2"),
        ]
        mocked_print.assert_has_calls(expected_calls)
        self.assertEqual(5, mocked_print.call_count)

    @patch("builtins.print")
    def test_search_book_finds_multiple_books_with_same_title(self, mocked_print):
        """
        Verifies search output when more than one book has the same title.
        """
        self.store.books = [self.book_a, self.book_b, self.book_c]

        self.store.search_book("Python 101")

        expected_calls = [
            unittest.mock.call("Found 2 book(s) with title 'Python 101':"),
            unittest.mock.call("Title: Python 101"),
            unittest.mock.call("Author: Mike"),
            unittest.mock.call("Price: $15.0"),
            unittest.mock.call("Quantity: 2"),
            unittest.mock.call("Title: Python 101"),
            unittest.mock.call("Author: Laura"),
            unittest.mock.call("Price: $18.0"),
            unittest.mock.call("Quantity: 1"),
        ]
        mocked_print.assert_has_calls(expected_calls)
        self.assertEqual(9, mocked_print.call_count)

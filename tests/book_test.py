import unittest
from models.book import Book

class TestBook (unittest.TestCase):

    def setUp(self): 
        self.book = Book("Undoctored", "Adam Kay", False, "still to be read", 2)

    def test_book_has_title(self):
        expected = "Undoctored"
        actual = self.book.title
        self.assertEqual(expected, actual)

    def test_book_has_author(self):
        expected = "Adam Kay"
        actual = self.book.author
        self.assertEqual(expected, actual)

    def test_book_completed_start_false(self):
        expected = False
        actual = self.book.completed
        self.assertEqual(expected, actual)

    def test_has_note(self):
        self.book = Book("Undoctored", "Adam Kay", False, "Book is great", 2)
        expected = "Book is great"
        actual = self.book.notes
        self.assertEqual(expected, actual)

    def test_has_id(self):
        expected = 2
        actual = self.book.id
        self.assertEqual(expected, actual)

    def test_has_no_id(self):
        self.book = Book("Undoctored", "Adam Kay")
        expected = None
        actual = self.book.id
        self.assertEqual(expected, actual)


    def test_book_can_mark_book_as__not_complete(self):
        self.book.mark_completed(False)
        expected = False
        actual = self.book.completed
        self.assertEqual(expected, actual)

    def test_book_can_mark_book_as_complete(self):
        self.book.mark_completed(True)
        expected = True
        actual = self.book.completed
        self.assertEqual(expected, actual)
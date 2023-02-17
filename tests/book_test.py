import unittest
from models.book import Book

class TestBook (unittest.TestCase):

    def setUp(self): 
        self.book = Book("Undoctored", "Adam Kay")

    def test_book_has_title(self):
        expected = "Undoctored"
        actual = self.book.title
        self.assertEqual(expected, actual)


    def test_book_has_author(self):
        expected = "Adam Kay"
        actual = self.book.author
        self.assertEqual(expected, actual)

    def test_book_has_author(self):
        expected = "Adam Kay"
        actual = self.book.author
        self.assertEqual(expected, actual)

    def test_book_completed_start_false(self):
        expected = False
        actual = self.book.completed
        self.assertEqual(expected, actual)
import unittest
from models.book import Book

class TestBook (unittest.TestCase):

    def setUp(self): 
        self.book = Book("Undoctored", "Adam Kay")

    def test_book_has_title(self):
        expected = "Undoctored"
        actual = self.book.title
        self.assertEqual(expected, actual)
import unittest
from models.author import Author


class TestAuthor (unittest.TestCase):

    def setUp(self):
        self.author = Author("Adam", "Kay", 1)

    def test_author_has_first_name(self):
        expected = "Adam"
        actual = self.author.first_name
        self.assertEqual(expected, actual)

    def test_author_has_last_name(self):
        expected = "Kay"
        actual = self.author.last_name
        self.assertEqual(expected, actual)

    def test_has_id(self):
        expected = 1
        actual = self.author.id
        self.assertEqual(expected, actual)

    
    def test_has_no_id(self):
        self.author = Author("Adam", "Kay")
        expected = None
        actual = self.author.id
        self.assertEqual(expected, actual)

    def test_author_has_full_name(self):
        self.author.full_name()
        expected = "Adam Kay"
        actual = self.author.full_name()
        self.assertEqual(expected, actual)

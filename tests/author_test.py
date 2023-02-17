import unittest
from models.author import Author


class TestAuthor (unittest.TestCase):

    def setUp(self):
        self.author = Author("Adam", "Kay")

    def test_author_has_first_name(self):
        expected = "Adam"
        actual = self.author.first_name
        self.assertEqual(expected, actual)

    def test_author_has_last_name(self):
        expected = "Kay"
        actual = self.author.last_name
        self.assertEqual(expected, actual)
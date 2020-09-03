from unittest import TestCase
from book import Book


class TestBook(TestCase):

    def setUp(self):
        self.book = Book("test book", "test author")

    def test_init(self):
        self.assertEqual(self.book.book_title, "test book")
        self.assertEqual(self.book.author, "test author")


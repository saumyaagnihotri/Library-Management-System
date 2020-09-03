from unittest import TestCase

from book import Book
from transaction import Transaction
from student import Student

class TestTransaction(TestCase):
    def setUp(self):
        self.transaction = Transaction(book = Book("tbook", "tauthor"), student= Student("tname"), status = "Book Issued", date = "02/09/2020")

    def test_init(self):
        self.assertEqual(self.transaction.book_title, "tbook")
        self.assertEqual(self.transaction.student_name, "tname")


#    def test_transaction(self):
#        self.fail()

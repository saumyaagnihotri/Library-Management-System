from unittest import TestCase
from library_db import LibraryDB
from book import Book
from staff import Staff


class TestStaff(TestCase):


    def setUp(self):
        self.staff = Staff()

    def test_add_book(self):
        self.staff.add_book("tbook", "tauthor")
        self.assertEqual((LibraryDB.book_list[-1]).book_title, "tbook")
        self.assertEqual((LibraryDB.book_list[-1]).author, "tauthor")



"""
    def test_view_report(self):
    self.fail()

    def test_delete_book(self):
        self.fail()

    def test_add_book(self):
        self.fail()
        
"""

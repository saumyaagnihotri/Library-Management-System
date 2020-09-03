import itertools

from library_db import LibraryDB
from transaction import Transaction


class Student:

    id_iter = itertools.count()
    id_iter.__next__()

    def __init__(self, name):
        self.student_id = next(Student.id_iter)
        self.name = name
        self.fine = 0
        self.issued_books = []
        LibraryDB.student_list.append(self)

    @staticmethod
    def view_books():

        """Function to display list of books available

        :return: None
        """
        flag = 0
        for book in LibraryDB.book_list:
            if book.availability:
                book.student_display()
                flag = 1
        if not flag:
            print("No books are available in the catalogue!")
            return 0
        else:
            return 1

    def validate_bookid(self,book_id):

        """Function to validate input book id

        :param book_id: int
        :return: Boolean
        """
        if int(book_id) in [i.book_id for i in self.issued_books]:
            return True
        else:
            return False

    @staticmethod
    def calculate_fine(book):
        """This method calculates the fine.

        :param book: Book Object
        :return: int : fine calculated


        """
        days = (book.return_date - book.issue_date).days
        if days > 15:
            return (days - 15) * 20
        else:
            return 0

    def issue_book(self, book_id, issue_date):
        """This method performs the book issue operation

        :param book_id: Book auto generated Id
        :type book_id: Book
        :param issue_date: Date of issuing the book
        :type issue_date: date
        :return: None


        """
        for book in LibraryDB.book_list:
            if book.book_id == book_id:
                book.availability = False
                book.issue_date = issue_date
                self.issued_books += [book]
                # Transaction(book, self, "Book Issued")
                date = book.issue_date.strftime('%b %d, %Y')
                LibraryDB.transaction_history.append(Transaction(book, self, "Book Issued", str(date)))
                print("Book Issued!")
                break
        else:
            print("Book with this id is not available!")

    def return_book(self, book_id, return_date):

        """Function to perform return book operation

        :param book_id: id of the book
        :param return_date: return date
        :return: None
        """
        for book in LibraryDB.book_list:
            if book.book_id == book_id and book_id in [i.book_id for i in self.issued_books]:
                book.availability = True
                book.return_date = return_date
                result = self.calculate_fine(book)
                self.fine += result
                self.issued_books.remove(book)
                date = book.return_date.strftime('%b %d, %Y')
                LibraryDB.transaction_history.append(Transaction(book, self, "Book Returned",str(date)))
                if result == 0:
                    print("Book returned on time!")
                else:
                    print("Book returned!" + "\n" + "Fine amount : " + str(result) + '\n')
                break
        else:
            print("Please enter a valid id")

    def total_books_issued(self):

        return len(self.issued_books)

    def my_books(self):
        for book in self.issued_books:
            book.student_display()

    def __str__(self):
        return str(self.student_id) + ", " + self.name

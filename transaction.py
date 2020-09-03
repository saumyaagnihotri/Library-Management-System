import itertools


class Transaction:
    id_iter = itertools.count()
    id_iter.__next__()

    def __init__(self, book, student, status, date):
        self.transaction_id = next(Transaction.id_iter)
        self.book_title = book.book_title
        self.student_name = student.name
        self.status = status
        self.date = date

    def __str__(self):
        return "Transaction Id = " + str(self.transaction_id) + ", " + \
               "Book Title = " + self.book_title + ", " + \
               "Student Name = " + self.student_name + ", " + \
               "Status = " + self.status + ", " + \
               "Date = " + self.date

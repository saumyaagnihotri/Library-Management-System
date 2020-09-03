import itertools

from library_db import LibraryDB


class Book:
    id_iter = itertools.count()
    id_iter.__next__()

    def __init__(self, book_title, author):
        self.book_id = next(Book.id_iter)
        self.book_title = book_title
        self.author = author
        self.availability = True
        self.issue_date = None
        self.return_date = None
        LibraryDB.book_list.append(self)

    def student_display(self):
        print(*["Book Id = ", self.book_id, ", Book Title = ", self.book_title, ", Author = ", self.author], sep=" ")

    def __str__(self):
        return "Book Id" + str(self.book_id) + ", " + \
               "Book Title" + self.book_title + ", " + \
               "Author" + self.author + ", " + \
               "Availability" + str(self.availability)


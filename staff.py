from book import Book
from library_db import LibraryDB


class Staff:
    def __init__(self):
        pass

    @staticmethod
    def view_report():
        flag = 0
        for transaction in LibraryDB.transaction_history:
            print(transaction)
            flag = 1
        if not flag:
            print("No data in the transaction list! \n")

    @staticmethod
    def delete_book(book_id):
        for book in LibraryDB.book_list:
            if book.book_id == book_id and book.availability:
                LibraryDB.book_list.remove(book)
                print("Book has been deleted from the catalogue\n")
                break
        else:
            print("Book with this id is not available currently!")

    @staticmethod
    def add_book(book_name, author):
        Book(book_name, author)
        print("Book has been added")
        # LibraryDB.book_list.append(book)


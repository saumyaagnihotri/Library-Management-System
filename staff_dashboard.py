from library_db import LibraryDB
from staff import Staff


def staff_dashboard():

    """Function to display options for staff member
    :return: None
    """

    print("STAFF DASHBOARD")
    print("1. Add books")
    print("2. Delete books")
    print("3. View Transactions")
    print("4. Back to home page")
    print("5. Exit")
    ch = int(input())
    staff = Staff()
    while True:
        if ch == 1:
            print("Enter the title of the book : ")
            book_title = input()
            print("Enter the author name : ")
            author = input()
            staff.add_book(book_title, author)

        elif ch == 2:
            print(*[book for book in LibraryDB.book_list], sep="\n")
            print("Enter the id of the book you want to delete : ")
            req_id = int(input())
            staff.delete_book(req_id)

        elif ch == 3:
            staff.view_report()

        elif ch == 4:
            return

        else:
            exit()

        print("\nSTAFF DASHBOARD")
        print("1. Add books")
        print("2. Delete books")
        print("3. View Transactions")
        print("4. Back to home page")
        print("5. Exit")
        ch = int(input())


from library_db import LibraryDB
from student import Student
from datetime import date

def student_dashboard():

    """Function to display options for student


    :return:
    """
    print("STUDENT DASHBOARD")
    print("1. New User")
    print("2. Registered User")
    print("3. Back to home page")
    print("4. Exit")

    new_student = None
    ch = int(input())
    if ch == 1:
        print("Enter you name")
        name = input()
        new_student = Student(name)
        print("Registered successfully! User Id : " + str(new_student.student_id) + "\n")
    elif ch == 2:
        print("Enter your id")
        new_id = int(input())
        for student in LibraryDB.student_list:
            if student.student_id == new_id:
                new_student = student
                print("Welcome, " + student.name + "!\n")
                break
        else:
            print("Invalid ID")
            return
    elif ch == 3:
        return
    else:
        exit()

    print("\nSTUDENT DASHBOARD")
    print("1. View Books")
    print("2. Issued Books")
    print("3. Return Books")
    print("4. View total fine")
    print("5. Back to home page")
    print("6. Exit")
    ch = int(input())
    while True:
        if ch == 1:
            result = Student.view_books()
            if new_student.total_books_issued() == 2:
                print("Cannot issue any more books (Max limit = 2)")
            elif result:
                print("Enter the book id you want to request :")
                req_id = int(input())
                print("Enter the date (dd/mm/yyyy): ")
                issue_date = input().split('/')
                issue_date = date(int(issue_date[2]), int(issue_date[1]), int(issue_date[0]))
                new_student.issue_book(req_id, issue_date)

        elif ch == 2:
            if(new_student.total_books_issued()==0):
                print("No data in the issued book list!")
            else:
                new_student.my_books()
        elif ch == 3:
            print("Enter the book id you want to return : ")
            req_id = int(input())
            if not new_student.validate_bookid(req_id):
                print("Invalid ID!\n")
            else:
                print("Enter the date (dd/mm/yyyy): ")
                return_date = input().split('/')
                return_date = date(int(return_date[2]), int(return_date[1]), int(return_date[0]))
                new_student.return_book(req_id, return_date)
        elif ch == 4:
            print("Your total fine amount is : " + str(new_student.fine) + '\n')
        elif ch == 5:
            return
        else:
            exit()

        print("\nSTUDENT DASHBOARD")
        print("1. View Books")
        print("2. Issued Books")
        print("3. Return Books")
        print("4. View total fine")
        print("5. Back to home page")
        print("6. Exit")
        ch = int(input())


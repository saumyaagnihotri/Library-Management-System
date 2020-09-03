from book import Book
from staff_dashboard import staff_dashboard
from student_dashboard import student_dashboard
import csv

def init_db():
    with open('db/BookDB') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            Book(row[0], row[1])


def home():

    """ Function with 2 branch redirection
    :return: None

    """
    init_db()
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Student")
    print("2. Staff")
    print("3. Exit")
    ch = int(input())
    while True:
        if ch == 1:
            student_dashboard()
        elif ch == 2:
            staff_dashboard()
        else:
            exit()

        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("1. Student")
        print("2. Staff")
        print("3. Exit")
        ch = int(input())


home()

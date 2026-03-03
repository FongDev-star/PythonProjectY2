from file_handler import load_students
from ui import header, line, pause


def search_student():
    header("SEARCH STUDENT BY ID")

    students = load_students()

    student_id = input("Enter Student ID: ").strip()

    for s in students:
        if s[0] == student_id:
            line("-")
            print(f"ID     : {s[0]}")
            print(f"Name   : {s[1]}")
            print(f"Age    : {s[2]}")
            print(f"Gender : {s[3]}")
            print(f"Major  : {s[4]}")
            line("-")
            pause()
            return
    print("Student not found.")
    pause()
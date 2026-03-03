from file_handler import load_students, save_students
from ui import pause

def update_student():
    students = load_students()
    student_id = input("Enter ID to edit: ").strip()

    for student in students:
        if student[0] == student_id:
            student[1] = input("New Name: ")
            student[2] = input("New Age: ")
            student[3] = input("New Gender: ")
            student[4] = input("New Major: ")

            save_students(students)
            print("Student updated succesfully!")
            pause()
            return
    print("Student not found.")
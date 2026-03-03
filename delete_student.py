from file_handler import load_students, save_students
from ui import pause

def delete_student():
    students = load_students()
    student_id = input("Enter ID to delete: ").strip()

    new_students = [s for s in students if s[0] != student_id]

    if len(new_students) == len(students):
        print("Student not found.")
    else:
        save_students(new_students)
        print("Student deleted successfully!")
        pause()
        
        
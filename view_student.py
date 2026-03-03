from file_handler import load_students
from ui import header, line, pause

def view_student():
    header("STUDENT LIST")

    students = load_students()

    if not students:
        print("No students found.")
        return

    print(f"{'ID':<10}{'Name':<20}{'Age':<6}{'Gender':<10}{'Major':<15}")
    line("-")

    for s in students:
        print(f"{s[0]:<10}{s[1]:<20}{s[2]:<6}{s[3]:<10}{s[4]:<15}")

    line("-")
    pause()
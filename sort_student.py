from file_handler import load_students, save_students
from ui import header, line, pause


def sort_student():
    header("SORT STUDENTS")

    students = load_students()

    if not students:
        print("No students available.")
        return

    print("1. Sort by ID")
    print("2. Sort by Name")
    line("-")

    choice = input("Choose option: ")

    if choice == "1":
        students.sort(key=lambda x: x[0])
    elif choice == "2":
        students.sort(key=lambda x: x[1].lower())
    else:
        print("Invalid choice.")
        return
    save_students(students)

    print("\nSorted Result:\n")
    print(f"{'ID':<10}{'Name':<20}{'Age':<6}{'Gender':<10}{'Major':<15}")
    line("-")
    
    for s in students:
        print(f"{s[0]:<10}{s[1]:<20}{s[2]:<6}{s[3]:<10}{s[4]:<15}")

    line("-")
    pause()
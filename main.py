from add_student import add_students
from view_student import view_student
from update_student import update_student
from delete_student import delete_student
from search_student import search_student
from sort_student import sort_student
from ui import show_menu, line

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_students()
        elif choice == "2":
            view_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            sort_student()
        elif choice == "0":
            line()
            print("Program exiting...")
            print("Thank you for using the system")
            line()
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
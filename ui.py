import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def line(char="=", length=60):
    print(char * length)

def header(title):
    clear_screen()
    line()
    print(title.center(60))
    line()
def pause():
    input('\nPlease enter to continue...')
    
def show_menu():
    header("STUDENT MANAGEMENT SYSTEM")

    print("1. Add New Student")
    print("2. View All Students")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Sort Student")
    print("0. Exit")
    line()
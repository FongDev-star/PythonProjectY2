from file_handler import load_students, append_student
from ui import pause, line

def add_students():
    students = load_students()
    student_id = (input("Enter student id: ")).strip()
    
    if any(s[0] == student_id for s in students):
        print('student id already exists.')
        return
    
    student_name = input("Enter Name: ").strip()
    student_age = input("Enter Age: ").strip()
    student_gender = input("Enter Gender: ").strip()
    student_major = input("Enter Major: ").strip()
    
    if not student_age.isdigit():
        print('Age must be a number!')
        return
    
    append_student([student_id, student_name, student_age, student_gender, student_major])
    print('Student added successfully!')
    pause()


    
    
    
        
    
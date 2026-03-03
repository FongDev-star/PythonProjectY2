import os

file_name = 'student.txt'

def load_students():
    students = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) == 5:
                    students.append(data)
    return students

def save_students(students):
    with open(file_name, 'w') as file:
        for student in students:
            file.write('|'.join(student) + '\n')

def append_student(student):
    with open(file_name, 'a') as file:
        file.write('|'.join(student) + '\n')
    
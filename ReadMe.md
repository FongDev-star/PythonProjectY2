STUDENT MANAGEMENT SYSTEM
==========================

HOW TO RUN THE PROGRAM:
-----------------------
1. Ensure you have Python installed (Python 3.6 or higher recommended)
2. Save all Python files in the same directory:
   - main.py
   - ui.py
   - file_handler.py
   - add_student.py
   - view_student.py
   - update_student.py
   - delete_student.py
   - search_student.py
   - sort_student.py
3. The program will automatically create/use 'student.txt' for data storage
4. Open terminal/command prompt in the directory
5. Run: python main.py

FEATURES IMPLEMENTED:
---------------------
- Add New Student - Add student with ID, Name, Age, Gender, Major
- View All Students - Display all students in formatted table
- Edit Student - Update existing student information
- Delete Student - Remove student by ID
- Search Student - Find and display student by ID
- Sort Students - Sort by ID or Name (alphabetically)
- Persistent Storage - Data saved in student.txt file
- Clean Console UI - Clear screen and formatted output
- Input Validation - Age must be numeric, duplicate ID checking

KNOWN BUGS/LIMITATIONS:
-----------------------
- No validation for empty inputs
- Gender and Major fields accept any text (no dropdown/enumeration)
- Sort by Name is case-insensitive but doesn't handle special characters
- ID is treated as string, so "100" and "0100" are different
- No data backup before edit/delete operations
- Age validation only checks if numeric, not age range
- Cannot export data to other formats (CSV, Excel, etc.)
- No confirmation prompt before deleting
- Search only works by ID, not by name or other fields
- Screen clearing may not work in all IDEs/terminals
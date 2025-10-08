student_grades = {}

def add_students(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' added with grade {grade}.")

def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student '{name}' removed.")
    else: 
        print(f"Student '{name}' not found.")

def display_students():
    print("All Students:")
    for name, grade in student_grades.items():
        print(f"{name}, {grade}")

def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade updated to {grade}.")
    else:
        print("Student not found")

add_students("Max", 65)
add_students("John", 95)
add_students("Grace", 79)

display_students()

remove_student("Grace")

update_grade("Max", 85)

print(student_grades)

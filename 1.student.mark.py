#Define functions

def input_student_data():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth (YYYY-MM-DD): ")
    return (student_id, student_name, student_dob)

def input_course_data():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)

def input_course_marks(course, students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} in {course[1]}: "))
        marks[student[0]] = mark
        return marks

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def show_marks(course, students, marks):
    print(f"Marks for {course[1]}:")
    for student in students:
        print(f"{student[1]}: {marks.get(student[0], '-')}")

#Main program

num_students = int(input("Enter the number of students in the class: "))

students = []
for i in range(num_students):
    print(f"\nEnter information for student {i+1}:")
    student = input_student_data()
    students.append(student)

num_courses = int(input("\nEnter the number of courses: "))

courses = []
for i in range(num_courses):
    print(f"\nEnter information for course {i+1}:")
    course = input_course_data()
    courses.append(course)

course_marks = {}
for course in courses:
    print(f"\nInput marks for course {course[1]}:")
    marks = input_course_marks(course, students)
    course_marks[course[0]] = marks

list_courses(courses)

list_students(students)

course_id = input("Enter course ID to show marks: ")
course = next((c for c in courses if c[0] == course_id), None)
if course:
    marks = course_marks.get(course_id)
    show_marks(course, students, marks)
else:
    print("Invalid course ID.")

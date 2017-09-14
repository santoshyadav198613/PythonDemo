students = []


def get_students_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase = student["name"].title()
    return  students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, id=1):
    student = {"name": name, "id": id}
    students.append(student)


student_name = input("Enter Student Name:")
student_id = input("Enter Student Id:")

add_student(student_name, student_id)
print_students_titlecase()

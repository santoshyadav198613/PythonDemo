students = []

def get_students_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase = student.title()
    return  students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, id=1):
    student= { "name": name , "id": id }
    students.append(student)

def var_args(name, *args):
    print(name)
    print(args)



def var_args_desc(name, **kwargs):
    print(name)
    print(kwargs["desc"], kwargs["message"])


add_student("Santosh", 50)

add_student(name="Sam", id= 52)

var_args("sam", "test", None, "hello")

var_args_desc("sam", desc= "test", feedback= None, message= "hello")


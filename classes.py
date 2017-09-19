students = []


class Student:
    school_name = "Test"

    def __init__(self, name, id=1):  # constructor
        student = {"name": name, "id": id}
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_caps(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


santosh = Student("Santosh", 5)
print(santosh.name)
print(Student.school_name)


class HighStudent(Student):  #inheritance
    school_name = "High School";

    def get_name_caps(self):  #Overloading
        school_hsname = super().get_name_caps();
        return  school_hsname+  "-HS"

sam= HighStudent("Sam")
print(sam.get_name_caps())

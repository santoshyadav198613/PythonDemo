from student import  Student


class HighStudent(Student):  #inheritance
    school_name = "High School";

    def get_name_caps(self):  #Overloading
        school_hsname = super().get_name_caps();
        return  school_hsname+  "-HS"
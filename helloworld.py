print('Hello World')

number = 5;
if number == 5 and True:
    print("this is true")
else:
    print("number is not equals to 5");


studentList = ["Sam", "hiya", "test"];

for student in studentList:
    print('student name {0}'.format(student));

employee = {"name": "Test", "id": 1, "age": 10, "last_name": "test"}

try:
    lastName = employee["last_name"]
    print(lastName);
    number_last_name = 3+ lastName;
except KeyError:
    print("Error Finding Last Name")
except TypeError as error:
    print("Trying to add different value types {0}".format(error))
except Exception:
    print("Some error occurred")

print("Code executed");






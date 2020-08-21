class Student:
    def __new__(cls, *args):
        new_student = object.__new__(cls)
        print("Student __new__ gets called")
        return new_student

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print("Student __init__ gets called")


student = Student("John Miller", "M")

class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"Student({self.name!r}, {self.gender!r})"

    def __str__(self):
        return f"Student: {self.name}, {self.gender}"

student = Student("John Miller", "M")
repr(student)
evaluated = eval(repr(student))
type(evaluated)

print(student)
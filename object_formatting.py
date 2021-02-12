# class Student:
#     def __init__(self, name):
#         self.name = name
#
#
# student0 = Student("John Smith")
# student0

class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"

student0 = Student("John Smith")
student0
print(student0)

student1 = eval(repr(student0))
student1

name = "John Smith"
print(f"Student({name!r})")
print(f"Student({name})")

from io import BytesIO

BytesIO(b'Medium')

with open("test.text", 'w') as file:
    print(repr(file))

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "__str__ is called"

student0 = Student("John Smith")
print(student0)
f"{student0}"


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}, {self.name}"


student0 = Student("John Smith")
print(student0)


class Student:
    def __init__(self, name):
        self.name = name

    def __format__(self, format_spec):
        return "__format__ is called"

student0 = Student("John Smith")
f"{student0}"
format(student0)
print(student0)
str(student0)


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}, {self.name}"

    def __format__(self, format_spec):
        if format_spec == "i":
            return "".join(x[0] for x in self.name.split())
        elif format_spec == "C":
            return self.name.upper()
        print("___delegate to the built-in format method for generic formatting___")
        return format(str(self), format_spec)


student0 = Student("John Smith")
print("format_spec: i", f"{student0:i}")
print("format_spec: C", f"{student0:C}")
print("format_spec: generic", f"{student0:-^30}")

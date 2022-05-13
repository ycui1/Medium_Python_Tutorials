name = "Danny"
age = 15
student = {"name": name}
scores = [100, 99, 95]
location = ('123 Main', 'NY')
for item in (name, age, student, scores, location):
    print(f"{type(item)!s: <15}| repr: {repr(item): <20}| str: {str(item)}")
    

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return "Student __repr__ string"
    
    def __str__(self):
        return "Student __str__ string"
    

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def __repr__(self):
            return f"Student({self.name!r}, {self.age})"
        
        def __str__(self):
            return f"Student Name: {self.name}; Age: {self.age}"
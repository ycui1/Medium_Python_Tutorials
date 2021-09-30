5 + 3 * 4
(5 + 3) * 4

5 > 2 and 9 > 7
5 > (2 and 9) > 7
(5 > 2) and (9 > 7)


# Define a simple function
def hello_world():
    print("Hello, World!")

hello_world
hello_world()

int()
str()
dict()
set()
list()
tuple()


class Person:
    def __init__(self, name):
        self.name = name


person = Person("John Smith")
person

# Function is callable
callable(hello_world)
# Class is callable
callable(Person)
# String is not callable
name = "John Smith"
callable(name)

import inspect
inspect.getmro(Person)

id(person)
hash(person)


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

employee = Employee("David Smith", 123456)

inspect.getmro(Employee)

tuple()

# Create an empty tuple
()
# Create a single-element tuple
(5,)
# Create a tuple with multiple elements
(5, 3)

print("Type of (5):", type((5)))
print("Type of (5,):", type((5,)))


def simple_generator():
    x = 0
    while x < 4:
        yield x*x
        x += 1


number_gen = simple_generator()
for number in number_gen:
    print("Current Squares:", number)

number_gen = (x*x for x in range(4))
for number in number_gen:
    print("Current Squares:", number)

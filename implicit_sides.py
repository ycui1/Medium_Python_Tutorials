# Instance Method Invocation
class Person:
    def speak(self):
        print(f"Speak method is called by {self}")


person0 = Person()
person0.speak()

# Special Methods
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        print("__len__ is invoked")
        return self.age

    def __abs__(self):
        return

person1 = Person1("John Smith", 38)
len(person1)
abs(person1)


# Create a decorator function
def alert(func):
    def wrapper(*args, **kwargs):
        print(f"Alert: {func.__name__} is being called.")
        return func(*args, **kwargs)

    return wrapper


# Use the decorator with a function
@alert
def greeting(person):
    print(f"Hello, {person}!")


greeting("John")


def greeting1(person):
    print(f"Hello, {person}!")

greeting1 = alert(greeting1)
greeting1("John")

# Iterations
# A simple iteration
numbers = [1, 2]
for a in numbers:
    print(a)


class PerfectSquare:
    def __init__(self, limit):
        self.limit = limit
        self.n = 1

    def __iter__(self):
        print("Creating an iterator")
        return self

    def __next__(self):
        print("Getting the next item")
        if self.n < self.limit:
            square = self.n * self.n
            self.n += 1
            return square
        else:
            print("Complete iteration")
            raise StopIteration


for number in PerfectSquare(4):
    print(number)
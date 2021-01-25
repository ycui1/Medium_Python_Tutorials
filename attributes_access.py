class Person:
    def __init__(self, name):
        self._name = name

    def set_name(self, value):
        self._name = value

    def get_name(self):
        return self._name


class Person1:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

person = Person("Mike")
person.get_name()
person.set_name("Mike Smith")

person1 = Person1("Mike")
person1.name
person1.name = "Mike Smith"


class Person2:
    def __init__(self, name):
        self.name = name


person2 = Person2("Mike")
person2.name
person2.name = "Mike Smith"

class Person3:
    def __init__(self, name):
        self.name = name
        self._name = f"_{name}"
        self.__name = f"__{name}"


person3 = Person3("Mike")
person3._name
person3._Person3__name

class Person4:
    def __init__(self, name):
        self.name = name

    def find_relatives(self):
        # a pseudo function for get the relatives from a server
        self.relatives = get_relatives_from_database()
        return self.relatives


class Person5:
    def __init__(self, name):
        self.name = name
        self.relatives = None

    def find_relatives(self):
        # the same as above Person4
        pass


class Person6:
    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Sorry, but you can't be younger than a newborn.")
        self._age = value
        print("Set age to", value)


person6 = Person6("Mike")
person6.age = 20
person6.age = -1

class Person7:
    def __init__(self, name):
        self.name = name
        self.age = None

    def __setattr__(self, key, value):
        if key == "age" and value is not None and value < 0:
            raise ValueError("Sorry, but you can't be younger than a newborn.")
        print(f"Set {key} to {value}")
        super().__setattr__(key, value)

person7 = Person7("Mike")
person7.age = 20
person7.age = -5

class Person8:
    def __init__(self):
        pass

def foo():
    print("Foo Foo")

def bar():
    print("Bar Bar")

person8 = Person8()
person8.speak = foo
person8.speak = bar

person8.speak()

person8.speak.__name__


class Person9:
    def __init__(self):
        pass

person9 = Person9()

def working_function():
    print("version 1")
person9.working_function = working_function

person9.working_function()


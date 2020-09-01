# Create an empty list
a_list = list()
# Create an empty dictionary
a_dict = dict()
# Create an empty set
a_set = set()
# Create an empty tuple
a_tuple = tuple()

class Person:
    def __new__(cls, *args):
        new_person = object.__new__(cls)
        print("Person __new__ gets called")
        print(f"Person Instance Memory Address: {id(new_person)}")
        return new_person

    def __init__(self, name):
        print(self.__dict__)
        self.name = name
        print("Person __init__ gets called")
        print(f"Set Initial State: {id(self)}")
        print(self.__dict__)

    def __del__(self):
        print(f"The object is getting deleted: {self}")

def remove(person):
    print(f"The object is getting deleted: {person}")

person = Person("John")

globals().keys()

globals()['person']
id(globals()['person'])
hex(id(person))

import sys
import gc

# With the sys module
sys.getrefcount(person)

# With the gc module
len(gc.get_referrers(person))

gc.get_referrers(person)[0] == globals()

# Create an object that references to the person variable
family = {'household head': person}
len(gc.get_referrers(person))

# Delete the object that references to the person variable
del family
len(gc.get_referrers(person))

'person' in globals()
del person
'person' in globals()

len(gc.get_referrers(person))

person = Person("John")
id(person)
del person

found_object = None
for obj in gc.get_objects():
    if id(obj) == 4505270688:
        print("found")
        found_object = obj

print(found_object)

person0 = Person("John")
person1 = person0
id(person0) == id(person1)

del person0
del person1
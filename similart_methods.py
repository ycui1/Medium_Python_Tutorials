# sorted() for any iterable
sorted([7, 4, 3, 2], reverse=True)
sorted({7: 'seven', 2: 'two'})
sorted([('nine', 9), ('one', 1)], key=lambda x: x[-1])
sorted('hello')

# sort() for a list
grades = [{'name': 'John', 'grade': 99},
          {'name': 'Mary', 'grade': 95},
          {'name': 'Zack', 'grade': 97}]
grades.sort(key=lambda x: x['grade'], reverse=True)
grades

# reversed() for any sequence data
reversed([1, 2, 3])
list(reversed((1, 2, 3)))
tuple(reversed('hello'))

# reverse() for a list
numbers = [1, 2, 3, 4]
numbers.reverse()
numbers

# Create a list object to begin with
integers = [1, 2, 3]

# append()
integers.append(4)
integers.append([5, 6])
integers

# extend()
integers.extend({7, 8, 9})
integers.extend('hello')
integers


# Create a function for comparison
def compare_two_objects(obj0, obj1):
    print("obj0 id:", id(obj0), "obj1 id:", id(obj1))
    print("Compare Identity:", obj0 is obj1)
    print("Compare Value:", obj0 == obj1)

compare_two_objects([1, 2, 3], [1, 2, 3])
compare_two_objects([1, 2].reverse(), None)

# Create a list of integers
integers = [1, 2, 3, 4, 5]

# remove()
integers.remove(1)
integers

# pop()
integers.pop()
integers
integers.pop(0)
integers

# clear()
integers.clear()
integers

[1, 2, 3, 4].remove(5)
[].pop()
[].clear()

# Create a function to check iterables
def check_any_all(iterable):
    print(f"any({iterable!r}): {any(iterable)}")
    print(f"all({iterable!r}): {all(iterable)}")

check_any_all([1, False, 2])
check_any_all([True, True, True])
check_any_all(tuple())

# Create a function to check set relationship
def check_set_relation(set0, set1):
    print(f"Is {set0} a superset of {set1}?", set0.issuperset(set1))
    print(f"Is {set0} a subset of {set1}?", set0.issubset(set1))
check_set_relation({1, 2, 3}, {2, 3})
check_set_relation({3, 4}, {3, 4, 5})

# Create two lists for zipping
list0 = [1, 2, 3]
list1 = ['a', 'b', 'c', 'd', 'e']

# Zip two lists with zip()
zipped0 = list(zip(list0, list1))
zipped0

# Zip two lists with zip_longest()
from itertools import zip_longest
zipped1 = list(zip_longest(list0, list1))
zipped1
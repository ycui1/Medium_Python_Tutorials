# An iterable to start with
numbers = ['one', 'two', 'three']

# The basic way
for i in range(len(numbers)):
    print(f"# {i + 1}: {numbers[i]}")

# Use enumerate()
for i, number in enumerate(numbers, 1):
    print(f"# {i}: {number}")

# Two iterables
students = ["John", "David", "Ashley"]
scores = [95, 93, 94]

# The basic way
for i in range(len(students)):
    student = students[i]
    score = scores[i]
    print(f"Student {student}: {score}")

# Use zip()
for student, score in zip(students, scores):
    print(f"Student {student}: {score}")

# The students arrival records
students_arrived = ["John", "David", "Ashley"]

# The typical ways
for i in range(1, len(students_arrived)+1):
    print(students_arrived[-i])

for student in students_arrived[::-1]:
    print(student)

# Use reversed()
for student in reversed(students_arrived):
    print(student)

# A list of numbers to process
numbers = [1, 3, 4, 8, 9]

# The typical way
for number in numbers:
    if number % 2:
        print(f"Do operations with odd number: {number}")

# Use filter()
for number in filter(lambda x: x % 2, numbers):
    print(f"Do operations with odd number: {number}")

from itertools import chain

# A few iterables to begin with
odd_numbers = [1, 3]
even_numbers = [2, 4]

# The typical way
numbers = odd_numbers + even_numbers
for number in numbers:
    print(f"Operate with number: {number}")

# Use chain()
for number in chain(odd_numbers, even_numbers):
    print(f"Operate with number: {number}")

# The dictionary object
grades = {"John": 99, "Danny": 95, "Ashley": 98}

# Iterate the keys
for name in grades:
    print(name)
for name in grades.keys():
    print(name)

# Iterate the values
for grade in grades.values():
    print(grade)

# Iterate the items: key-value pairs
for name, grade in grades.items():
    print(f"{name}: {grade}")

# Current keys
names = grades.keys()
print(f"Before updating: {names}")

# Add a new item and check the same view object
grades['Jennifer'] = 97
print(f"After updating: {names}")

# A list of numbers
primes = [2, 3, 5]

# List Comprehension
# Instead of the following
squares_list0 = list()
for prime in primes:
    squares_list0.append(prime * prime)
# Do this
squares_list1 = [x * x for x in primes]

# Dictionary Comprehension
# Instead of the following
squares_dict0 = dict()
for prime in primes:
    squares_dict0[prime] = prime*prime
# Do this
squares_dict1 = {x: x*x for x in primes}

# Set Comprehension
# Instead of the following
squares_set0 = set()
for prime in primes:
    squares_set0.add(prime)
# Do this
squares_set1 = {x*x for x in primes}


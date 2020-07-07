i_str = 'Hello'
i_list = [0, 1]
i_tuple = (404, 'No Data')
i_dict = {'zero': 0, 'one': 1}
i_set = {'John', 'Danny'}
iterables = [i_str, i_list, i_tuple, i_dict, i_set]

for iterable in iterables:
    print(f"*** Start to iterate over an iterable of {type(iterable)}")
    for i, item in enumerate(iterable, 1):
        print(item, end='__' if i < len(iterable) else '\n')


# Create a list of integers
integers = list(range(10))
print(f'* List: {integers}')

# Create a tuple of integers
numbers = tuple(integers)
print(f'* Tuple: {numbers}')

# Create a dictionary
items = [('zero', 0), ('one', 1), ('two', 2)]
words = dict(items)
print(f'* Dict: {words}')

# Create a set
evens = (-2, 4, 2, 0, 2, -4, 4)
unique_evens = set(evens)
print(f'* Set: {unique_evens}')

# List Comprehension
[expression for item in iterable if optional_condition]

# Dictionary Comprehension
{key_expr: value_expr for item in iterable if optional_condition}

# Set Comprehension
{expression for item in iterable if optional_condition}


# Create an iterable to start with for all comprehensions
numbers = list(range(-3, 4))
print(f'Initial Iterable: {numbers}')

# List comprehension
squares_list = [x*x for x in numbers]
print(f'* listcomp: {squares_list}')

# Dictionary comprehension
squares_dict = {x: x*x for x in numbers if x % 2 == 0}
print(f'* dictcomp: {squares_dict}')

# Dictionary comprehension
squares_set = {x*x for x in numbers}
print(f'* setcomp: {squares_set}')


# Generator Expression Syntax
# (expression for x in iterable)

# Compare generators vs. lists
squares_gen = (x*x for x in range(1000000))
print(f'* Size of Generator: {squares_gen.__sizeof__()}')

squares_list = [x*x for x in range(1000000)]
print(f'* Size of List: {squares_list.__sizeof__()}')

sum_gen = sum(squares_gen)
sum_list = sum(squares_list)
print(f'# Sum of Squares Using Generator: {sum_gen}')
print(f'# Sum of Squares Using List: {sum_list}')


numbers = [0, 1, 2]
letters = ('x', 'y', 'z')

number0, number1, number2 = numbers
letter0, letter1, letter2 = letters

print(f'* Numbers: {number0}, {number1}, {number2}')
print(f'* Letters: {letter0}, {letter1}, {letter2}')

more_numbers = list(range(10))
first_number, *middle_numbers, last_number = more_numbers
print(f'* First Number: {first_number}')
print(f'* Middle Numbers: {middle_numbers}')
print(f'* Last Number: {last_number}')

# How to use the filter function
# filter(filtering_func, iterable)

# Use the filter function
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21]
filtered_fibonacci = filter(lambda x: x % 3 == 0, fibonacci)
print(f'Filter Object: {filtered_fibonacci}')
print(f'Filter Type: {type(filtered_fibonacci)}')

for item in filtered_fibonacci:
    print(f'Item: {item}')


# How to use the map function
# map(mapping_func, *iterables)

# Use the filter function
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21]
mapped_fibonacci = map(lambda x: f'1/{x}', fibonacci)
print(f'Map Object: {mapped_fibonacci}')
print(f'Map Type: {type(mapped_fibonacci)}')

for item in mapped_fibonacci:
    print(f'Mapped Item: {item}')


import numpy as np
import pandas as pd

# Create a numpy array from a list
numbers = [1, 2, 3, 4, 5, 6]
num_array = np.array(numbers)
print('* Numpy Array:', num_array, '\n')

# Create a pd Series from a list
names = ['John', 'Zack', 'Danny']
names_series = pd.Series(names)
print('* pd Series:\n', names_series, '\n')

# Create a pd DataFrame from a dictionary
grades = {'name': names, 'grade': [99, 100, 98]}
grades_df = pd.DataFrame(grades)
print('* pd DataFrame:\n', grades_df)

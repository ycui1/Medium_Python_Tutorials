# Define a function to calculate the mean using the def keyword
def calculate_mean(numbers):
    # Takes a list of integers
    number_sum = sum(numbers)
    number_count = len(numbers)
    number_mean = number_sum / number_count
    # return the calculated mean of the list of integers
    print(f"The mean of {numbers} is {number_mean}.")
    return number_mean


# Use the function
calculate_mean([1, 2, 3, 4])

message0 = "Hello"
message1 = "World"
print(message0, message1, end="@@\n", sep=",")
print(end="@@\n", message0, message1)

# Create a list of numbers for sorting
numbers = [3, 11, 7, 5]
# Sort the numbers by default
sorted(numbers)
# Sort the numbers by their remainders when divided by 3
sorted(numbers, key=lambda x:x % 3)

# Use the dict constructor
dict(a=1, b=2, c=3)
dict(a=4, b=5, c=6)

# Example with a custom function
def send_info(**kwargs):
    for key, value in kwargs.items():
        print(f"parameter name: {key}; value: {value}")

send_info(name="John", age=16)
send_info(first_name="John", last_name="Smith")


import pandas as pd
# Create a data series
old_ids = pd.Series("prefix1001 prefix1002 prefix1003".split(), name="old_id")
print(old_ids)
# Create a data series by removing the prefix and creating a number
new_ids = old_ids.map(lambda x: int(x[6:]))
print(new_ids)

# Create a function that accepts two arguments
def greeting(word, person):
    print(f"{word}, {person}!")

greeting("Hi", "John")
greeting("Hi", "Danny")

# Create a partial function
from functools import partial
say_hi = partial(greeting, "Hi")
say_hi("John")
say_hi("Danny")

say_hi

def make_incrementer(step):
    # Track the count
    counter = 0
    # Define the incrementer function
    def incrementer():
        nonlocal counter
        counter += step
        return counter
    # Return the incrementer function
    return incrementer

incrementer_ten = make_incrementer(10)

incrementer_ten.__code__.co_freevars
incrementer_ten.__closure__[0].cell_contents
incrementer_ten()
incrementer_ten.__closure__[0].cell_contents
incrementer_ten()
incrementer_ten.__closure__[0].cell_contents

import time
def logging_time(func):
    """Decorator that logs time"""
    def logger():
        """Function that logs time"""
        start = time.time()
        func()
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")

    return logger

@logging_time
def calculate_sum():
    return sum(range(10000))

calculate_sum()

calculate_sum
calculate_sum.__code__.co_freevars
calculate_sum.__closure__
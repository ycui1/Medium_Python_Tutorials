# Declare a list of tuples
scores = [('John', 95), ('Danny', 98), ('Aaron', 90), ('Leo', 94)]
# Sort using the default order of the tuples
sorted(scores, reverse=True)
# Sort using the scores
sorted(scores, key=lambda x: x[1], reverse=True)

# Create a list to be used in comprehensions
numbers = [1, 2, 3, -3, -2, -1]
# Create a new list of these numbers' squares
[x*x for x in numbers]
# Create a new dictionary of these numbers' exponentiation
{x: pow(10, x) for x in numbers}
# Create a set of these numbers' absolutes
{abs(x) for x in numbers}


# A trivial generator function
def abc_generator():
    yield "a"
    yield "b"
    yield "c"


abc_gen = abc_generator()
print("Type of abc_gen:", type(abc_gen))
for letter in abc_gen:
    print(letter)

# integer_list = list(range(1000000000))
#
# import sys
# sys.getsizeof(integer_list)
#
# del integer_list


limit = 10000000000

# Use a generator function
def integer_generator():
    n = 0
    while n < limit:
        n += 1
        yield n


int_gen = integer_generator()
int_sum0 = sum(int_gen)

# Use generator expression
int_sum1 = sum(x for x in range(1, limit+1))


from functools import wraps
import time


def timing(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time Elapsed: {end-start}")

    return wrapped


@timing
def sum_of_squares(n):
    int_sum = sum(x*x for x in range(n))
    print(f"Sum of Squares from 1 to {n}: {int_sum}")


sum_of_squares(100)
sum_of_squares(10000000)


import random
import timeit


# Create a function to check the look up time
def dict_look_up_time(n):
    numbers = list(range(n))
    random.shuffle(numbers)
    d0 = {x: str(x) for x in numbers}
    random_int = random.randint(0, n - 1)
    t0 = timeit.timeit(lambda: d0[random_int], number=10000)
    return t0


for n in (10, 100, 1000, 10000, 100000):
    elapse_time = dict_look_up_time(n)
    print(f"*** N = {n:<8}: {elapse_time:.5f}")
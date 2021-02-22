# Type hints
def format_personal_info(name: str, age: int) -> dict:
    person = {"Name": name, "Age": age}
    return person

user = format_personal_info("John Smith", 25)


# Advanced type hints
from typing import Optional


def process_data(required: dict, optional: Optional[int]):
    pass


required_data = {1: 1}
process_data(required_data, 15)
process_data(required_data, None)
process_data(required_data, "zero")


# Keyword-only arguments
def add_numbers(a, b, deduction=0):
    total = a + b - deduction
    return total


add_numbers(5, 7, 20)
add_numbers(5, 7, deduction=20)

def add_numbers_better(a, b, *, deduction=0):
    total = a + b - deduction
    return total

add_numbers_better(5, 7, 20)
add_numbers_better(5, 7, deduction=20)


# Decorators
import time
from functools import wraps, lru_cache


def logging_time(func):
    @wraps(func)
    def logger(*args, **kwargs):
        start = time.time()
        output_value = func(*args, **kwargs)
        print(f"Calling {func.__name__} with {args}: {time.time() - start:.5f}")
        return output_value
    return logger


@logging_time
def calculate_sum_n(n):
    return sum(range(n))


@logging_time
@lru_cache
def calculate_fib(n):
    if n <= 2:
        return 1
    return calculate_fib(n-1) + calculate_fib(n-2)

calculate_fib(4)
calculate_fib(5)
calculate_fib(5)

class Person:
    def speak(self):
        pass

    def _walk(self):
        pass

    def __sleep(self):
        pass

person = Person()
person.speak()
person._walk()
person._Person__sleep()
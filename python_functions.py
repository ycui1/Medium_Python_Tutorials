def doubler(a):
    return a * 2


doubler.__name__

numbers = [1, 2, 3]
mapped = map(doubler, numbers)
list(mapped)

from_print = print("message")
print(from_print)

print("a message", end=";", sep="|")


def create_fraction(a, b):
    return a / b


create_fraction(b=2, a=3)


def multiplier(a, by=1, offset=0):
    return a * by - offset


multiplier(5, 2, 1)


def multiplier_keyword(a, *, by=1, offset=0):
    return a * by - offset


multiplier_keyword(5, 2, 1)
multiplier_keyword(5, by=2, offset=1)


def custom_sum_pos(iterable, /, start=0):
    result = sum(iterable) + start
    return result


custom_sum_pos([1, 2, 3], start=10)
custom_sum_pos(iterable=[1, 2, 3], start=10)

print("Hello", "World", "Python")


def greet(*persons, word="Hi"):
    print("Persons:", persons)
    print("Type:", type(persons))
    message = word + ", " + ", ".join(persons)
    print(message)


greet("Aaron", "John", "Jennifer")


def mean_score(**scores):
    print("Scores:", scores)
    print("Type:", type(scores))
    average_score = sum(scores.values()) / len(scores)
    print("Mean Score:", average_score)


mean_score(John=99, Jennifer=97, Aaron=95)


def simple_generator():
    x = 1
    while x < 4:
        yield x
        x += 1


num_gen = simple_generator()
numbers = list(num_gen)
print(numbers)


def make_incrementer(step):
    counter = 0

    def incrementer():
        nonlocal counter
        counter += step
        return counter

    return incrementer


incrementer = make_incrementer(5)
incrementer.__code__.co_freevars

from asyncio.tasks import sleep
import time
from typing import AsyncContextManager


def logging_time(func):
    def logger(*args, **kwargs):
        start = time.time()
        returned = func(*args, **kwargs)
        end = time.time()
        print(f"Calling {func.__name__} time: {end - start:.5f}")
        return returned

    return logger


@logging_time
def calculate_sum(n):
    return sum(range(n + 1))


calculate_sum(10000)

number = 1
number = "one"


def single_dict(key: int, value: str) -> dict:
    return {key: value}


numbers = [1, 2, 3, 4, 5]
numbers.pop()
numbers


class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"The student {self.name} is studying.")

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def students_from_list(cls, names):
        return [cls(name) for name in names]


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def employee_price(self):
        return self.price * 0.9


vacuum = Product("Vacuum", 200)
vacuum.employee_price


class Product:
    def _adjust_price(self):
        print("This is a protected method.")

    def __order_more(self):
        print("This is a private method")


product = Product()
product._Product__order_more()

numbers = [1, 2, 3, 4, 5]
numbers.__sizeof__()


class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student({self.name!r})"


student = Student("John")
student

grades = [("John", [95, 94, 89]), ("Jen", [83, 100, 98]), ("Zoe", [95, 88, 93])]
sorted(grades, key=lambda x: sum(x[1]))

from functools import partial


def incrementer(start, step):
    return start + step


incrementer_by_one = partial(incrementer, step=1)

incrementer_by_one(5)

import time


def login_user():
    time.sleep(2)


def load_posts():
    time.sleep(3)


def launch_app():
    print("Open App:", time.asctime())
    login_user()
    load_posts()
    print("App Page Loaded:", time.asctime())


launch_app()

import asyncio


async def login_user_async():
    await asyncio.sleep(2)


async def load_posts_async():
    await asyncio.sleep(3)


async def launch_app_async():
    print("Open App:", time.asctime())
    await asyncio.gather(
        login_user_async(),
        load_posts_async()
    )
    print("App Page Loaded:", time.asctime())


asyncio.run(launch_app_async())
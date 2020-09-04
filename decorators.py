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

@logging_time
def calculate_sum_n(n):
    return sum(range(n))

calculate_sum_n(10000)






import time
from functools import wraps

def logging_time(func):
    """Decorator that logs time"""
    @wraps(func)
    def logger(*args, **kwargs):
        """Function that logs time"""
        start = time.time()
        func(*args, **kwargs)
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")

    return logger

@logging_time
def calculate_sum_n(n):
    return sum(range(n))

@logging_time
def say_hi(whom, greeting="Hello"):
    print(f"{greeting}, {whom}!")

calculate_sum_n(100000)
say_hi("John", greeting="Hi")


import time
from functools import wraps

def logging_time(func):
    """Decorator that logs time"""
    @wraps(func)
    def logger(*args, **kwargs):
        """Function that logs time"""
        start = time.time()
        func(*args, **kwargs)
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")

    return logger


@logging_time
def say_hello(whom):
    """Greet someone"""
    print(f"Hello, {whom}!")

print(say_hello.__doc__)


import time
from functools import wraps

def logging_time(unit):
    """Decorator that logs time"""
    def logger(func):
        @wraps(func)
        def inner_logger(*args, **kwargs):
            """Function that logs time"""
            start = time.time()
            func(*args, **kwargs)
            scaling = 1000 if unit == "ms" else 1
            print(f"Calling {func.__name__}: {(time.time() - start) * scaling:.5f} {unit}")

        return inner_logger

    return logger


@logging_time("ms")
def calculate_sum_ms(n):
    """Calculate sum of 0 to n-1"""
    return sum(range(n))

@logging_time("s")
def calculate_sum_s(n):
    """Calculate sum of 0 to n-1"""
    return sum(range(n))


calculate_sum_ms(100000)
calculate_sum_s(100000)


def repeat(func):
    """Decorator that repeats function call twice"""
    def repeater(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return repeater


@logging_time("ms")
@repeat
def say_hi(whom):
    print(f"Hi, {whom}!")


@repeat
@logging_time("ms")
def say_hello(whom):
    print(f"Hello, {whom}!")

say_hi("John")
say_hello("Aaron")


class Repeat:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        def repeater(*args, **kwargs):
            for _ in range(self.n):
                func(*args, **kwargs)

        return repeater

@Repeat(n=2)
def morning_greet(person):
    print(f"Good Morning, {person}!")

@Repeat(n=3)
def afternoon_greet(person):
    print(f"Good Afternoon, {person}!")

morning_greet("Jason")
afternoon_greet("Kelly")
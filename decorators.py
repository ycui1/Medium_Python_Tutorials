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



calculate_sum.__closure__[0].cell_contents
calculate_sum.__code__.co_freevars

# Decorator that repeats function call twice
def repeat(func):
    def repeater(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return repeater

@repeat
def say_hi(whom):
    print(f"Hello, {whom}!")

say_hi("John")

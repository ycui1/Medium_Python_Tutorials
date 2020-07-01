def invocation_log(func):
    def inner_func(*args, **kwargs):
        """Inner function within the invocation_log"""
        print(f'Before Calling {func.__name__}')
        func(*args, **kwargs)
        print(f'After Calling {func.__name__}')

    return inner_func


@invocation_log
def say_hello(name):
    """Say hello to someone"""
    print(f"Hello, {name}!")

# Call the decorated function
say_hello("John")

print(say_hello)

# def say_hello_no_decoration(name):
#     """Say hello to someone"""
#     print(f"Hello, {name}!")
#
# say_hello = invocation_log(say_hello_no_decoration)


help(say_hello)

print(say_hello.__doc__)

import pickle
print(pickle.dumps(say_hello))


from functools import wraps


def invocation_log(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        """Inner function within the invocation_log"""
        print(f'Before Calling {func.__name__}')
        func(*args, **kwargs)
        print(f'After Calling {func.__name__}')

    return inner_func


@invocation_log
def say_hello(name):
    """Say hello to someone"""
    print(f"Hello, {name}!")


# Call the decorated function
say_hello("John")

import pickle


def check_decorator_wraps(decorated_func):
    print(decorated_func)
    help(decorated_func)
    print(decorated_func.__doc__)
    print(pickle.dumps(decorated_func))


check_decorator_wraps(say_hello)





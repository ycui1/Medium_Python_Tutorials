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


print(say_hello)
help(say_hello)
print(say_hello.__doc__)
import pickle
print(pickle.dumps(say_hello))

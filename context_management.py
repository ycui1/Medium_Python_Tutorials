with open('hello.txt', 'w') as file:
    file.write("Hello World!")

with open('hello.txt', 'r') as file:
    text = file.read()
    print('Text in the file:', text)


with open('hello.txt', 'a') as file:
    file.write('\nHello Python!')

closed = file.closed
print("Is the file closed?", closed)

# Append some new data
file0 = open("hello.txt", "a")
file0.write("\nHello World Again!")

# Read the file again
file1 = open("hello.txt")
print(file1.read())

try:
    # open the file and create the object
    file = open('hello.txt')
    # do particular operations
except Exception:
    # handle any possible exceptions
    raise
finally:
    # Release the file
    file.close()


from threading import Lock

# Use the with statement
with Lock():
    # do your operations here
    pass

# Without the with statement
lock = Lock()
lock.acquire()
try:
    # do your operations here
    pass
except Exception:
    # handle exceptions
    pass
finally:
    lock.release()

class ContextManagerExample:
    def __init__(self):
        print("Context Manager Created")

    def __enter__(self):
        print("Begin Context Management")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End Context Management")


with ContextManagerExample():
    print("Run operations in the with statement")


def invocation_log(func):
    def inner_func(*args, **kwargs):
        print(f'Before Calling {func.__name__}')
        func(*args, **kwargs)
        print(f'After Calling {func.__name__}')

    return inner_func


@invocation_log
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Python")


from contextlib import contextmanager

@contextmanager
def context_manager_example():
    print("Create the context")
    yield
    print("Destroy the context")


with context_manager_example():
    print("Run operations with the context")

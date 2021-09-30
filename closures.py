# 07/27/2021
def multiplier_creator(n):
    def multiplier(number):
        return number * n

    return multiplier


double_multiplier = multiplier_creator(2)
triple_multiplier = multiplier_creator(3)

del multiplier_creator
double_multiplier(5)
triple_multiplier(5)

double_multiplier.__code__.co_freevars
double_multiplier.__closure__[0].cell_contents

triple_multiplier.__code__.co_freevars
triple_multiplier.__closure__[0].cell_contents


def running_total_multiplier_creator(n):
    running_total = 0
    def multiplier(number):
        nonlocal running_total
        product = number * n
        running_total += product
        return running_total

    return multiplier


running_doubler = running_total_multiplier_creator(2)
running_doubler(5)


def simple_logger(func):
    def decorated(*args, **kwargs):
        print(f"You're about to call {func}")
        result = func(*args, **kwargs)
        print(f"You just called {func}")
        return result

    return decorated


@simple_logger
def hello_world():
    print("Hello, World!")


hello_world()
hello_world.__code__.co_freevars
hello_world.__closure__[0].cell_contents


def say_hello(name):
    greeting = f"Hello, {name}!"
    return greeting


greeting = say_hello("Python")
print(greeting)


def greeting_creator(greeting_word):
    def greet(name):
        return f"{greeting_word}, {name}"

    return greet

say_hi = greeting_creator("Hi")

# To show the list of nonlocal variables
print("Free Variables:", say_hi.__code__.co_freevars)
# To show the value of the nonlocal variable
print("Value of the free variable:", say_hi.__closure__[0].cell_contents)


# Create another closure
say_hey = greeting_creator("Hey")

# To show the list of nonlocal variables
print("Free Variables:", say_hey.__code__.co_freevars)
# To show the value of the nonlocal variable
print("Value of the free variable:", say_hey.__closure__[0].cell_contents)


def evil_greeting_creator(greeting_word):
    def greet(name):
        nonlocal greeting_word
        greeting_word = "Non-" + greeting_word
        return f"{greeting_word}, {name}"

    return greet

say_dear = evil_greeting_creator("Dear")
print(say_dear("Johnny"))


def echo(func):
    def inner_fun():
        func()
        func()

    return inner_fun


@echo
def say_good_morning():
    print("Good Morning!")


say_good_morning()

print(say_good_morning.__code__.co_freevars)
print(say_good_morning.__closure__[0].cell_contents)

def say_good_afternoon():
    print("Good Afternoon")


echoed_say_good_afternoon = echo(say_good_afternoon)
echoed_say_good_afternoon()
print(say_good_morning.__code__.co_freevars)
print(say_good_morning.__closure__[0].cell_contents)
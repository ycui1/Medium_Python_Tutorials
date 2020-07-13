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
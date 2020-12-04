with open("hello.txt", mode="w"):
    pass


def multiply(number, multiplier=1):
    return number * multiplier


multiply(5, multiplier=4)
multiply(5, 4)


def explicit_multiply(number, *, multiplier=1):
    return number * multiplier


explicit_multiply(5, multiplier=4)
explicit_multiply(5, 4)

# Function that has no strictly positional-only
def custom_sum(iterable, start=0):
    result = sum(iterable, start=start)
    return result

custom_sum([1, 2, 3], start=10)
custom_sum(iterable=[1, 2, 3], start=10)

# Function that has strictly positional-only
def custom_sum_pos(iterable, /, start=0):
    result = sum(iterable) + start
    return result

custom_sum_pos([1, 2, 3], start=10)
custom_sum_pos(iterable=[1, 2, 3], start=10)

def do_random_thing(arg1, /, arg2, *, arg3):
    print("Arguments Received:", [arg1, arg2, arg3])

do_random_thing(1, 2, arg3=3)
do_random_thing(1, arg2=2, arg3=3)
do_random_thing(arg1=1, arg2=2, arg3=3)

# Print one object
print("Hello")
# Print two objects
print("Hello", "World")
# Print two objects with specified separator
print("Hello", "World", sep=",")


def greet(*persons, greeting_word="Hi"):
    print("Persons to greet:", persons)
    print("Type of persons:", type(persons))
    message = greeting_word + ", " + ", ".join(persons)
    print(message)


greet("John", "Jennifer", "Aaron")

# Create dictionaries
dict(a=1, b=2)
dict(a=1, b=2, c=3)


def mean_grade(**grades):
    print("Grades for the total:", grades)
    print("Type of grades:", type(grades))
    total_grade = sum(grades.values())
    average_grade = total_grade / len(grades)
    print("Mean Grade:", average_grade)

mean_grade(John=99, Jennifer=97, Aaron=95)


# define a function involving the default value for a list
def append_score(score, scores=[]):
    scores.append(score)
    print(f"Scores: {scores}\nScores id: {id(scores)}")

append_score(98)
append_score(92, [100, 95])
append_score(94)

append_score.__defaults__

id(append_score.__defaults__[0])


def dispense_salary(employee, amount):
    """

    :param employee:
    :param amount:
    :return:
    """
    pass

dispense_salary()

def dispense_salary_typed(employee: str, amount: float):
    pass

dispense_salary_typed()

dispense_salary_typed(1, "amount")

def dispense_salary_typed(employee: str, amount: float=1000.0):
    """
    Dispense the salary to the employee
    :param employee: str, the name of the employee
    :param amount: float, the amount of the salary (default 1000.0)
    :return: None
    """
    pass

print(dispense_salary_typed.__doc__)

help(dispense_salary_typed)
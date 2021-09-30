# Too generic, wanting others to guess what it does??
def foo(): pass

# Lack of details, requiring contexts to understand
def do_step1(): pass

# Not following naming conventions, which should be snake style and all lowercase
def GETData(): pass

# A few explicit and meaningful names
def get_account_info(): pass

def generate_sales_report(): pass

# Embed all operations with one single function
def process_data():
    # a bunch of code to read data
    # a bunch of code to clean the data
    # a bunch of code to generate the report
    pass

# Refactor by create additional smaller functions
def read_data_from_path(filepath):
    return data

def clean_data(data):
    return cleaned_data

def generate_report(cleaned_data):
    return report

def process_data():
    data = read_data_from_path(filepath="path_to_file.csv")
    cleaned_data = clean_data(data)
    report = generate_report(cleaned_data)
    return report


# Set the price to the sale price or clearance sale with has addition discount
def set_regular_sale_price(price, discount):
    price *= discount
    return price


def set_clearance_sale_price(price, discount, additional_discount):
    sale_price = set_sale_price(price, discount)
    return sale_price * additional_discount


# A refactored combined function
def set_sale_price(price, discount, additional_discount=1):
    sale_price = price * discount
    return sale_price * additional_discount



def add_item_to_cart(new_item, shopper_name, existing_items=[]):
    existing_items.append(new_item)
    print(f"{shopper_name}'s cart has {existing_items}")
    return existing_items


shopping_list_wife = add_item_to_cart("Dress", "Jennifer")
shopping_list_husband = add_item_to_cart("Soccer", "David")

def add_item_to_cart(new_item, shopper_name, existing_items=None):
    if existing_items is None:
        existing_items = list()
    existing_items.append(new_item)
    print(f"{shopper_name}'s cart has {existing_items}")
    return existing_items

from statistics import mean, stdev

def evaluate_test_result(scores):
    scores_mean = mean(scores)
    scores_std = stdev(scores)
    return scores_mean, scores_std

evaluation_result = evaluate_test_result([1, 1, 1, 2, 2, 2, 6, 6, 6])
print(f"Evaluation Result ({type(evaluation_result)}): {evaluation_result}")

def get_data_from_file(filepath):
    try:
        with open(filepath) as file:
            computed_value = process_data(file)
    except Exception:
        return -1
    else:
        return computed_value

def process_data(file):
    # process the data
    return computed_value


# A list of dictionary objects for sorting
grades = [{'name': 'John', 'score': 97},
          {'name': 'David', 'score': 96},
          {'name': 'Jennifer', 'score': 98},
          {'name': 'Ashley', 'score': 94}]

def sorting_grade(x):
    return x['score']

sorted(grades, key=sorting_grade)

sorted(grades, key=lambda x: x['score'])

import pandas as pd

interest_rates = pd.Series([0.023, 0.025, 0.037])
interest_rates.map(lambda x: f"{x:.2%}")


# Define a decorator function
def echo_wrapper(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


# Define a function that is decorated by echo_wrapper
@echo_wrapper
def say_hello():
    print('Hello!')

# Call the decorated function
say_hello()


class Product:
    def __init__(self, item_id, price):
        self.item_id = item_id
        self.price = price

    @property
    def employee_price(self):
        return self.price * 0.9

product = Product(12345, 100)
product.employee_price

from time import time

# Create the decorator function
def logging_time(func):
    def logged(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f"{func.__name__} time elapsed: {elapsed_time:.5f}")

    return logged

@logging_time
def calculate_integer_sum(n):
    return sum(range(n))

@logging_time
def calculate_integer_square_sum(n):
    return sum(x*x for x in range(n))

calculate_integer_sum(10000)
calculate_integer_square_sum(10000)


# Define a function that accepts undetermined position arguments
def stringify(*args):
    return [str(x) for x in args]

stringify(2, False, None)

# Define a function that accepts undetermined keyword arguments
def generate_score_reports(name, **kwargs):
    print(f"***** Report for {name} *****")
    for key, value in kwargs.items():
        print(f"### {key}: {value}")
    print("***** Report End *****\n")

scores = {"John": {"math": 99, "phys": 97},
          "Jan": {"math": 94, "bio": 98}}

for name, scores in scores.items():
    generate_score_reports(name, **scores)

# Check type before running the code
def add_numbers(a, b):
    if not(isinstance(a, (float, int)) and isinstance(b, (float, int))):
        raise TypeError("Numbers are required.")
    return a + b

def add_five_no_annotation(x):
    return x + 5

add_five_no_annotation("1")

add_five_no_annotation("seven")


# Define a function with type annotation
def add_five_with_annotation(x: int) -> int:
    return x + 5


add_five_with_annotation("seven")
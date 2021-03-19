def hello_world():
    pass
    
hello_world()

numbers = [1, 2, 3]
numbers()

class Item:
    pass

Item()

callable(hello_world)
callable(numbers)
callable(Item)


integers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, integers))
squares

odds = list(filter(lambda x: x % 2, integers))
odds


numbers = [10, 2, 8, -7, -4]

def using_cubic(x):
    return x*x*x

sorted(numbers, key=using_cubic)

sorted(numbers, key=lambda x: x*x)


class PokerSorter(int):
    def __new__(cls, x):
        numbers_mapping = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        casted_number = numbers_mapping.get(x, x)
        return super().__new__(PokerSorter, casted_number)
       
       
cards = [10, 2, 'A', 'J', 7]

sorted(cards, key=PokerSorter)

import time

def logging_time(func):
    def logger(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")
        return result

    return logger

@logging_time
def calculate_sum_n(n):
    return sum(range(n))

calculate_sum_n(100000)


class TimeLogger:
    def __init__(self, func):
        def logger(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"Calling {func.__name__}: {time.time() - start:.5f}")
            return result
        self._logger = logger
        
    def __call__(self, *args, **kwargs):
        return self._logger(*args, **kwargs)
        
        
@TimeLogger
def calculate_sum_n_cls(n):
    return sum(range(n))


calculate_sum_n_cls(100000)

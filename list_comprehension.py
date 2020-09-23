# A list of integers
integers = [1, 2, 3, 4, 5, 6]
# Create a list of squares of only even numbers
squares = [x*x for x in filter(lambda x: x % 2 == 0, integers)]
squares = [x*x for x in integers if x % 2 == 0]
squares
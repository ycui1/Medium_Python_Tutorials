# A list of integers
integers = [1, 2, 3, 4, 5, 6]
# Create a list of squares and cubes
powers = [(x*x, pow(x, 3)) for x in integers]
print(powers)


# The same list of integers
integers = [1, 2, 3, 4, 5, 6]
# Create a list of squares for even numbers only
squares_of_evens = [x*x for x in integers if x % 2 == 0]
print((squares_of_evens))


# The list of integers
integers = [1, 2, 3, 4, 5, 6]
# Create a list of numbers, when the item is even, take the square
# when the item is odd, take the cube
custom_powers = [x*x if x % 2 == 0 else pow(x, 3) for x in integers]
print(custom_powers)

# Use the range object
integer_range = range(5)
[x*x for x in integer_range]
# Use the Series object
import pandas as pd
pd_series = pd.Series(range(5))
print(pd_series)
[x*x for x in pd_series]


# A list of tuples
prices = [('$5.99', '$4.99'), ('$3.5', '$4.5')]
# Flattened list of prices
prices_formatted = [float(x[1:]) for price_group in prices for x in price_group]
print(prices_formatted)


# A list of integers
integers = [1, 2, 3, 4, 5]
# Use map
squares_mapped = list(map(lambda x: x*x, integers))
# Use list comprehension
squares_listcomp = [x*x for x in integers]

# Use filter
filtered_filter = list(filter(lambda x: x % 2 == 0, integers))
# Use list comprehension
filterd_listcomp = [x for x in integers if x % 2 == 0]


# Create a list from a range object
numbers = [x for x in range(5)]
print(numbers)
# Create a list of lower-case characters from a string
letters = [x.lower() for x in 'Smith']
print(letters)

# Create a list from a range object
numbers = list(range(5))
print(numbers)
# Create a list of lower-case characters from a string
letters = list('Smith'.lower())
print(letters)

# Create the squares
squares = [x*x for x in range(10_000_000)]
# Calculate their sum
sum(squares)
squares.__sizeof__()

# Create the squares generator
squares_gen = (x*x for x in range(10_000_000))
# Calculate their sum
sum(squares_gen)
squares_gen.__sizeof__()
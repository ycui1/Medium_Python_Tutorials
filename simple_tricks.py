# Positive Indexing
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("First Number:", numbers[0])
print("First Four Numbers:", numbers[:4])
print("Odd Numbers:", numbers[::2])

# Negative Indexing
data_shape = (100, 50, 4)
names = ["John", "Aaron", "Mike", "Danny"]
hello = "Hello World!"

print(data_shape[-1])
print(names[-3:-1])
print(hello[1:-1:2])

if len(some_list) > 0:
    # do something here when the list is not empty
else:
    # do something else when the list is empty

# Container Emptiness
def check_container_empty(container):
    if container:
        print(f"{container} has elements.")
    else:
        print(f"{container} doesn't have elements.")

check_container_empty([1, 2, 3])
check_container_empty(set())
check_container_empty({"zero": 0, "one": 1})
check_container_empty(tuple())

# List of strings
# The typical way
columns = ['name', 'age', 'gender', 'address', 'account_type']
print("* Literals:", columns)

# Do this instead
columns = 'name age gender address account_type'.split()
print("* Split with spaces:", columns)

# If the strings contain spaces, you can use commas instead
columns = 'name, age, gender, address, account type'.split(', ')
print("* Split with commas:", columns)


# The typical way
if score > 90:
    reward = "1000 dollars"
else:
    reward = "500 dollars"

# Do this instead
reward = "1000 dollars" if score > 90 else "500 dollars"

# Another possible scenario
# You got a reward amount from somewhere else, but don't know if None/0 or not
reward = reward_known or "500 dollars"
# The above line of code is equivalent to below
reward = reward_known if reward_known else "500 dollars"

# Create a text file that has the text: Hello World!

# Open the file and append some new data
text_file0 = open("hello_world.txt", "a")
text_file0.write("Hello Python!")

# Open the file again for something else
text_file1 = open("hello_world.txt")
print(text_file1.read())

with open("hello_world.txt", "a") as file:
    file.write("Hello Python!")

with open("hello_world.txt") as file:
    print(file.read())

print("Is file close?", file.closed)


# Multiple Comparisons
# The typical way
if a < 4 and a > 1:
    # do something here

# Do this instead
if 1 < a < 4:
    # do somerthing here

# The typical way
if b == "Mon" or b == "Wed" or b == "Fri" or b == "Sun":
    # do something here

# Do this instead, you can also specify a tuple ("Mon", "Wed", "Fri", "Sun")
if b in "Mon Wed Fri Sun".split():
    # do something here

# The typical ways
if a < 10 and b > 5 and c == 4:
    # do something

if a < 10 or b > 5 or c == 4:
    # do something

# Do these instead
if all([a < 10, b > 5, c == 4]):
    # do something

if any([a < 10, b > 5, c == 4]):
    # do something

# The original form:
def generate_plot(data, image_name):
    """This function creates a scatter plot for the data"""
    # create the plot based on the data
    ...
    if image_name:
        # save the image
        ...

# In many cases, we don't need to save the image
generate_plot(data, None)

# The one with a default value
def generate_plot(data, image_name=None):
    pass

# Now, we can omit the second parameter
generate_plot(data)

words = ['an', 'boy', 'girl', 'an', 'boy', 'dog', 'cat', 'Dog', 'CAT', 'an',
         'GIRL', 'AN', 'dog', 'cat', 'cat', 'bag', 'BAG', 'BOY', 'boy', 'an']
unique_words = {x.lower() for x in set(words)}
for word in unique_words:
    print(f"* Count of {word}: {words.count(word)}")

from collections import Counter

word_counter = Counter(x.lower() for x in words)
print("Word Counts:", word_counter)

# Find out the most common item
print("Most Frequent:", word_counter.most_common(1))
# Find out the most common 2 items
print("Most Frequent:", word_counter.most_common(2))

# A list of numbers and strings
numbers = [1, 3, 7, 2, 5, 4]
words = ['yay', 'bill', 'zen', 'del']
# Sort them
print(sorted(numbers))
print(sorted(words))
# Sort them in descending order
print(sorted(numbers, reverse=True))
print(sorted(words, reverse=True))

# Create a list of tuples
grades = [('John', 95), ('Aaron', 99), ('Zack', 97), ('Don', 92),
          ('Jennifer', 100), ('Abby', 94), ('Zoe', 99), ('Dee', 93)]
# Sort by the grades, descending
sorted(grades, key=lambda x: x[1], reverse=True)
# Sort by the name's initial letter, ascending
sorted(grades, key=lambda x: x[0][0])

# Requirement: sort by name initial ascending, and by grades, descending
# Both won't work
sorted(grades, key=lambda x: (x[0][0], x[1]), reverse=True)
sorted(grades, key=lambda x: (x[0][0], x[1]), reverse=False)
# This will do the trick
sorted(grades, key=lambda x: (x[0][0], -x[1]))

student = {'name': "John", 'age': 18}
student['gender']

letters = ["a", "a", "c", "d", "d", "c", "a", "b"]
final_dict = {}
for letter in letters:
    if letter not in final_dict:
        final_dict[letter] = []
    final_dict[letter].append(letter)

print("Final Dict:", final_dict)

from collections import defaultdict

final_defaultdict = defaultdict(list)
for letter in letters:
    final_defaultdict[letter].append(letter)

print("Final Default Dict:", final_defaultdict)


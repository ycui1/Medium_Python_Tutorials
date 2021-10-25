fruits = ["pineapple", "banana", "grape"]
for fruit in fruits:
    print(fruit)

# enumerate the iterable
for item_i in range(len(fruits)):
    fruit = fruits[item_i]
    print(f"#{item_i+1}: {fruit}")

for item_i, fruit in enumerate(fruits, start=1):
    print(f"#{item_i}: {fruit}")

# reverse the iterable
fruits.reverse()
for fruit in fruits:
    print(fruit)

for fruit in reversed(fruits):
    print(fruit)

# sort the list
fruits.sort()
for fruit in fruits:
    print(fruit)

for fruit in sorted(fruits):
    print(fruit)

# zip the iterables
kids = ["John", "Zoe", "Ashley"]
for item_i, fruit in enumerate(fruits):
    kid = kids[item_i]
    print(f"{kid} likes {fruit}")

for kid, fruit in zip(kids, fruits):
    print(f"{kid} likes {fruit}")


for item in zip([1, 2], [10, 11, 12, 13]):
    print(item)

from itertools import zip_longest

for item in zip_longest([1, 2], [10, 11, 12, 13]):
    print(item)

# iterate a dict object
likes = {"John": "pineapple", "Zoe": "banana", "Ashley": "grape"}
for kid in likes:
    fruit = likes[kid]
    print(f"{kid} likes {fruit}")

for kid, fruit in likes.items():
    print(f"{kid} likes {fruit}")

# chain iterables
other_fruits = ["strawberry", "star fruit", "blackberry"]
all_fruits = fruits + other_fruits
for fruit in all_fruits:
    print(fruit)

from itertools import chain

for fruit in chain(fruits, other_fruits):
    print(fruit)

# map the items
for fruit in fruits:
    uppercase_fruit = fruit.upper()
    print(uppercase_fruit)

for fruit in map(str.upper, fruits):
    print(fruit)

# filter the items
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

for fruit in filter(lambda x: len(x) > 5, fruits):
    print(fruit)

# use break
def any_liked_fruit(fruits, liked_fruit):
    liked = False
    for fruit in fruits:
        print(f"Checking {fruit} likable")
        if not liked and fruit == liked_fruit:
            liked = True
    print("Found liked")
    return liked


any_liked_fruit(["apple", "pineapple", "orange"], "pineapple")


def any_like_fruit_break(fruits, liked_fruit):
    liked = False
    for fruit in fruits:
        print(f"Checking {fruit} likable")
        if fruit == liked_fruit:
            liked = True
            break
    print("Found liked")
    return liked


any_like_fruit_break(["apple", "pineapple", "orange"], "pineapple")


# use continue
for item in [1, 2, 3]:
    if item == 2:
        continue
    print(item)
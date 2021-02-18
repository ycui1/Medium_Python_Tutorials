# one-to-one unpacking
user_data = ("John", 44, "Male")
name, age, gender = user_data
print("User Name:", name)
print("User Age:", age)
print("User Gender:", gender)


# Access Individual Values Returned From a Function
def retrieve_user_posts(user_id):
    # call some functions to retrieve the data
    post_count = 20
    recent_posts = ["Post 1", "Post 2", "Post 3"]
    return post_count, recent_posts

total_count, latest_posts = retrieve_user_posts(123456)
print("Total Post Count:", total_count)
print("Latest Posts:", latest_posts)

# Use underscores for unwanted items
user_data = ("John", 44, "Male")
name, _, gender = user_data
print(f"Name: {name}; Gender: {gender}")

print(f"Age: {_}")

# User * to capture all
numbers = (1, 2, 3, 4, 5)
first_num, *middle_nums, last_num = numbers
print("First Number:", first_num)
print("Last Number:", last_num)
print("Remaining Numbers:", middle_nums)

first, *middle, last = (1, 2, 3)
print("Middle:", middle)
positive, *neutral, negative = ("+", "-")
print("Neutral:", neutral)

# Combine underscores and asterisks
many_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Good unpacking
one, *_, seven, eight, nine = many_numbers
print("Unwanted:", _)
# Bad unpacking
one, *_, middle, *big_nums, nine = many_numbers

# Tuple packing and unpacking in functions
def show_shopping_items(*items):
    print("Items:", items)
    print("Type of items:", type(items))
    for item in items:
        print(item)

show_shopping_items("Apple", "Banana")


grouping_factors1 = ("country", "state")
grouping_factors2 = (*grouping_factors1, "city")
print("Factors 1:", grouping_factors1)
print("Factors 2:", grouping_factors2)

id(grouping_factors1)
*grouping_factors1,

*"HI", "T"
*[1, 2, 3], 4
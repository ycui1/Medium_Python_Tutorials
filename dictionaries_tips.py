param0 = None
param1 = None


def fetch_params():
    global param0, param1
    param0 = "some value"
    param1 = "some other value"


params = dict.fromkeys(["param0", "param1"])


def fetch_params_dict():
    params["param0"] = "some value"
    params["param1"] = "some other value"


print(params)

# A list of tuples
items0 = [("a", 1), ("b", 2), ("c", 3)]
dict0 = dict(items0)
# A list of lists and tuples
items1 = [["a", 1], ["b", 2], ("c", 3)]
dict1 = dict(items1)
# A zip object
items2 = zip(["a", "b", "c"], [1, 2, 3])
dict2 = dict(items2)
# A tuple object
items3 = (["a", 1], ["b", 2], ("c", 3))
dict3 = dict(items3)
# Evaluation
dict0 == dict1 == dict2 == dict3

# Create a dictionary
existing_dict = {"a": 1, "b": 2, "c": 3}

# Create a list contains the keys only
list0 = list(existing_dict)
list1 = list(existing_dict.keys())
print(list0, list1)

# Create a list contains the values only
list2 = list(existing_dict.values())
print(list2)

# Create a list contains the key-value pairs
list3 = list(existing_dict.items())
print(list3)

sorted(existing_dict)
sorted(existing_dict.values())
sorted(existing_dict.items())

# Create a dictionary for iteration
iter_dict = {"a": 1, "b": 2}
for key in iter_dict:
    print(key)

for value in iter_dict.values():
    print(value)

for key, value in iter_dict.items():
    print(key, value)


messed_dict = {"c": 3, "b": 2, "a": 5}
for key, value in sorted(messed_dict.items()):
    print(key, value)

for value in sorted(messed_dict.values()):
    print(value)


ordered_dict = {"a": 1, "b": 2, "c": 3}
for value in reversed(ordered_dict.values()):
    print(value)

for key in reversed(ordered_dict):
    print(key)

# Create a list object
existing_list = [1, 2, 3]

# Create dictionary from the list
squares_dict = {x: x*x for x in existing_list}
print(squares_dict)

# Create a dictionary including only odd numbers
odds_dict = {x: x*x for x in existing_list if x % 2}
print(odds_dict)

# Create a dictionary object that tracks tips received for the day
tips = {'John': 35.5, 'Aaron': 40.75, 'Ashley': 39}
# Waiters are getting their own tips
def get_tip(waiter):
    tip_for_waiter = tips.pop(waiter)
    print(f"After dispensing ${tip_for_waiter} to {waiter}, \nthe remaining tips are ${tips}.")
    return tip_for_waiter

get_tip("John")
get_tip("Ashley")

tips.pop("Daniel")
tips.pop("Daniel", 0)

# Create a dictionary object that tracks tips received for the day
tips = {'John': 35.5, 'Aaron': 40.75, 'Ashley': 39}
# Destructively iterate the dictionary
while len(tips):
    waiter, tip = tips.popitem()
    print(f"After dispensing ${tip} to {waiter}, \nthe remaining tips are ${tips}.")

tips_all_dispensed = {}
tips_all_dispensed.popitem()

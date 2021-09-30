# Basic format of for loop
names = ["John", "Jack", "Jacob"]
for name in names:
    print(name)


def place_group_order(ordered_items):
    menu_items = ['beef', 'pork', 'sausage', 'chicken']
    for name, item in ordered_items.items():
        if item not in menu_items:
            print(f"Your group order can't be served, because {name}'s {item} isn't available.")
            break
    else:
        print("Your group order can be served.")


print("Group 0")
group0_items = {"John": "beef", "Jack": "tuna", "Jacob": "chicken"}
place_group_order(group0_items)

print("\nGroup 1")
group1_items = {"Aaron": "beef", "Ashley": "pork", "Anna": "sausage"}
place_group_order(group1_items)

# Basic Form of while Loop
saving_balance = 1000
while saving_balance > 0:
    saving_balance -= 200
    print(f"Withdrew 200 dollars, and remains: {saving_balance}")


def check_spending(alert_level):
    saving_balance = 1000
    while saving_balance > 0:
        if saving_balance < alert_level:
            print(f"Balance is less than {alert_level}. No more spending!")
            break
        saving_balance -= 200
        print(f"Withdrew 200 dollars, and remains: {saving_balance}")
    else:
        print("No more money is in the saving account.")


print("****Alert Level = 100")
check_spending(100)

print("\n****Alert Level = 500")
check_spending(500)

# Basic Form of try...except Statement
def cast_integer(num_text):
    try:
        number = int(num_text)
        print(f"{num_text!r} is casted to {number}.")
    except ValueError:
        print(f"You can't cast {num_text!r} to a number.")

print("***Cast a non-integer string")
cast_integer("zero")

print("\n***Cast an integer string ")
cast_integer("0")


def cast_integer_better(num_text):
    try:
        number = int(num_text)
    except ValueError:
        print(f"You can't cast {num_text!r} to a number.")
    else:
        print(f"{num_text!r} is casted to {number}.")
        return number


print("***Cast a non-integer string")
cast_integer_better("zero")

print("\n***Cast an integer string ")
cast_integer_better("0")
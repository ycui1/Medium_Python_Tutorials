# Negative Indexing
data_shape = (100, 50, 4)
names = ["John", "Aaron", "Mike", "Danny"]
hello = "Hello World!"

print(data_shape[-1])
print(names[-3:-1])
print(hello[-6:-1:2])

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

# Do this instead
columns = 'name age gender address account_type'.split()

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

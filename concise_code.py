#%%
# Use enumerate in for loops

# A list of guests
arrived_guests = ["John", "Ashley", "Danny", "Bobby"]

for guest in arrived_guests:
    arrived_order = arrived_guests.index(guest) + 1
    print(f"# {arrived_order}: {guest}")

for guest_i in range(len(arrived_guests)):
    guest = arrived_guests[guest_i]
    print(f"# {guest_i + 1}: {guest}")

for guest_i, guest in enumerate(arrived_guests, 1):
    print(f"# {guest_i}: {guest}")


# Proper ways to check containers' emptiness
# A list that we fetched from a server
fetched_data = []
if len(fetched_data) > 0:
    print("We fetched some data.")
else:
    print("We didn't fetch any data.")

if fetched_data != []:
    print("We fetched some data")
else:
    print("We didn't fetch any data")

if fetched_data:
    print("We fetched some data")
else:
    print("We didn't fetch any data")


# Use named tuples as data containers
# Use dictionaries
client0 = {"name": "John", "age": 37, "gender": "M"}
client1 = {"name": "Danny", "age": 41, "gender": "M"}
client2 = {"name": "Jennifer", "age": 34, "gender": "F"}


# Use a custom class
class Client:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


client0 = Client("John", 37, "M")
client1 = Client("Danny", 41, "M")
client2 = Client("Jennifer", 34, "F")

from collections import namedtuple

Client = namedtuple("Client", "name age gender")
client0 = Client("John", 37, "M")
client1 = Client("Danny", 41, "M")
client2 = Client("Jennifer", 34, "F")

type(Client)
issubclass(Client, tuple)

client0 = Client("John", 37, "M")
client0.name
client0.age
client0.gender


# A generic utility function
def save_image_to_directory(image_data, file_name, desired_directory):
    print(f"{image_data}, {file_name}, {desired_directory}")

# Event 0
save_image_to_directory("image_data0_101", "event0_101.png", "folder_for_event0")
save_image_to_directory("image_data0_102", "event0_102.png", "folder_for_event0")
# Many more invocations here and there

# Event 1
save_image_to_directory("image_data1_101", "event1_101.png", "folder_for_event1")
save_image_to_directory("image_data1_102", "event1_102.png", "folder_for_event1")
# Many more invocations here and there

from functools import partial

# Event 0
save_image_for_event0 = partial(save_image_to_directory, desired_directory='folder_for_event0')
save_image_for_event0("image_data0_101", "event0_101.png")
save_image_for_event0("image_data0_102", "event0_102.png")

# Event 1
save_image_for_event1 = partial(save_image_to_directory, desired_directory='folder_for_event1')
save_image_for_event1("image_data1_101", "event1_101.png")
save_image_for_event1("image_data1_102", "event1_102.png")


save_image_for_event2 = lambda x, y: save_image_to_directory(x, y, desired_directory='folder_for_event2')
save_image_for_event2("image_data2_101", "event2_101.png")

save_image_for_event1
save_image_for_event2
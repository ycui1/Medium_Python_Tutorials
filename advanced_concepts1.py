person = "Danny"
print("Hello, {}!".format(person))
print("Hello, %s!" % person)

price = 12.3507
sold_units = 2500
total_cost = price * sold_units
print("The price is ${:.2f}.\nThe # of sold units is {:,}.\nThe total cost is ${:,.2f}".format(price, sold_units, total_cost))

price = 12.3507
sold_units = 2500
total_cost = price * sold_units
print(f"The price is ${price:.2f}.\nThe # of sold units is {sold_units:,}.\nThe total cost is ${total_cost:,.2f}.")

class User:
    def __init__(self, username):
        self.username = username
        self._profile_data = None

    @property
    def profile_data(self):
        if self._profile_data is None:
            # Run the expensive web request function here
            fetched_data = get_data_remotely(self.username)
            self._profile_data = fetched_data
        return self._profile_data

# Create a list and calculate the sum
simple_list = [x*x for x in range(1000)]
print(f"Size: {simple_list.__sizeof__()} for type: {type(simple_list)}")
print(f"Sum: {sum(simple_list)}")

# Create a generate and calculate the sum
simple_gen = (x*x for x in range(1000))
print(f"Size: {simple_gen.__sizeof__()} for type: {type(simple_gen)}")
print(f"Sum: {sum(simple_gen)}")

# Use list comprehension
squares0 = [x*x for x in range(5)]
print(squares0)

# Use for loop
squares1 = []
for number in range(5):
    squares1.append(number*number)
print(squares1)

# Dictionary comprehension
squares_dict = {x: x*x for x in range(5)}
print(squares_dict)
# Set comprehension
squares_set = {x*x for x in range(-4, 5)}
print(squares_set)
number = 5
number = "five"

number = 5
type(number)
number = "five"
type(number)

# Create a variable and assign it with a number
a = 10000
# Get the memory address for this variable
id(a)
# Assign a string value to the "same" variable
a = "Medium"
# Get the memory address for this variable
id(a)

# Create a tuple object
api_response = (200, "data")
# Update one element
api_response[1] = "new data"

# Create a tuple object
http_response = (200, {"data": "some data"})
# Update one element's value
http_response[1]["data"] = "new data"
# The updated tuple
http_response


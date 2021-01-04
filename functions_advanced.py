# Define a function to calculate the mean using the def keyword
def calculate_mean(numbers):
    # Takes a list of integers
    number_sum = sum(numbers)
    number_count = len(numbers)
    number_mean = number_sum / number_count
    # return the calculated mean of the list of integers
    print(f"The mean of {numbers} is {number_mean}.")
    return number_mean


# Use the function
calculate_mean([1, 2, 3, 4])

message0 = "Hello"
message1 = "World"
print(message0, message1, end="@@\n", sep=",")
print(end="@@\n", message0, message1)


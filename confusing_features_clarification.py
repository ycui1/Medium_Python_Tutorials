number = 5 or 4
number

text = "" or "Hello, World!"
text

empty_string = ""
empty_list = []
what = empty_string or empty_list

number1 = 3 and 5
number1

text1 = "Hello" and "" and "World"
text1

text2 = "Hello" and "World" and "!"
text2

numbers = [1, 2, 3, 4]
eval(str(numbers))
eval("numbers = [1, 2, 3, 4]")

(numbers1 := [1, 2, 3])
eval("(numbers2 := [2, 3, 4])")

# A list of numbers that we need to calculate the sum
numbers = [1, 2, 3, 4]

# Calculate the accumulative sums
from itertools import accumulate
list(accumulate(numbers))

total = 0
[total := total + x for x in numbers]


with open("some_file.txt") as file:
    text_data = file.read()
  
# 1. Open the file
file = open("some_file.txt")

# 2. Perform some operations with the file
text_data = file.read()

# 3. Close the file
file.close()

file0 = open("file0.txt", "w")
file0.write("some random data")
print("Is the file0 closed?", file0.closed)

with open("file1.txt", "w") as file1:
    file1.write("some random data")

print("Is the file1 closed?", file1.closed)

from ast import pattern
from math import prod


greeting = "Hello, World!"

assert greeting[0] == "H"
assert greeting[1:3] == "el"

assert greeting[1:10:2] == 'el,Wr'

assert greeting[-1] == '!'
assert greeting[-3:-1] == "ld"

assert "Wor" in greeting

assert greeting.startswith("Hello")

assert greeting.endswith("ld!")

assert greeting.index("ello") == 1
assert greeting.find("ello") == 1

greeting.find("no_substr")
greeting.index("no_substr")

message = f"First Message: {greeting}"
print(message)

price = 1.23
volume = 12
product = "water"
description0 = "Product Name: " + product + "; Price: $" + str(price) + "; Volume: " + str(volume) + " oz"
print(description0)

description1 = f"Product Name: {product}; Price: ${price:}; Volume: {volume} oz"
assert description0 == description1

# Big numbers separator
big_number = 98765432123456789
assert f"{big_number:_d}" == '98_765_432_123_456_789'
# Floating numbers formatting
more_digits = 2.345678
assert f"{more_digits:.2f}" == '2.35'
assert f"{more_digits:.4f}" == '2.3457'
# Scientific notation
sci_number = 0.0000043203
assert f"{sci_number:e}" == '4.320300e-06'


s0, s1 = 'a', 'bb'

# Left-aligned with padding *
print(f'{s0:*<7}\n{s1:*<7}')

# Right-aligned with padding %
print(f'{s0:%>8}\n{s1:%>8}')

# Center-aligned
print(f'{s0:@^9}\n{s1:@^9}')




class Student:
    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

    def __repr__(self) -> str:
        print("__repr__ is invoked")
        return f"Student({self.name!r}, {self.grade})"

    def __str__(self) -> str:
        print("__str__ is called")
        return f"Student Name: {self.name}; Grade: {self.grade}"


student = Student("John Robinson", 6)
print(student)

import re

pattern = re.compile("^hi")

pattern.search("hi, Python")
pattern.search("hi, JavaScript")
pattern.search("hello, C#")


match = re.search(r"(\w\d)+", "xyzdda2b1c3ee")

print(match)
# output: <re.Match object; span=(5, 11), match='a2b1c3'>

print("matched:", match.group())
# output: matched: a2b1c3

print("span:", match.span())
# output: span: (5, 11)

print(f"start: {match.start()} & end: {match.end()}")
# output: start: 5 & end: 11


students_data = """101, John Robinson; good at maths
some random nonsense
102, Ashley Young; good at sports
54, random; record
103, Zoe Apple; All As
1234, random; record
Another random record"""

regex = re.compile(r"(\d{3}), (.+); (.+)")
desired_records = []
for line in students_data.split("\n"):
    match = regex.match(line)
    if match:
        print(f"{'Matched:':<12}{match.group()}")
        desired_records.append(line)
    else:
        print(f"{'No Match:':<12}{line}")

print(desired_records)


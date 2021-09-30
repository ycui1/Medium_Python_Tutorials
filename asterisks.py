pow(5, 3)
5**3

data = (1, 2, 3, 4)
a, b, c, d = data


a, *b = data
# a=1, b=[2, 3, 4]

shared_items = [1, 2, 3]

items1 = [*shared_items, 4, 5, 6]
items2 = [-3, -2, -1, *shared_items, 2, 4, 6]

[-3, -2, -1] + shared_items

[*range(3), 3, 4, 5]

shared_numbers = range(3)
[*shared_numbers, 3, 4, 5]
shared_numbers + [3, 4, 5]


def rounded_sum(*numbers):
    total = 0
    for number in numbers:
        total += round(number)
    print(f"Received {numbers} -> rounded sum: {total}")
    return total

rounded_sum(2.4, 3.7, 4.8)

science_scores = {"math": 90, "physics": 95, "chemistry": 92}
art_scores = {"english": 93, "spanish": 94}

combined_scores = {**science_scores, **art_scores}
print(combined_scores)

def send_info_to_server(**kwargs):
    print(f"Send the info: {kwargs}")
    # do something to prepare the information

send_info_to_server(postId="abc", userId="user")
send_info_to_server(like=True, status="success")


def multiply(number, multiplier=1):
    return number * multiplier

multiply(5, 4)
multiply(5, multiplier=4)





def explicit_multiply(number, *, multiplier=1):
    return number * multiplier


explicit_multiply(5, multiplier=4)
explicit_multiply(5, 4)
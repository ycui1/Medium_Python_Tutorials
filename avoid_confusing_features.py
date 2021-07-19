numbers = [2, 3, 5]
for number in numbers:
    print(f"Number: {number}")
else:
    print("All numbers are iterated.")

total = 3
while total > 0:
    total -= 1
    print(f"Total: {total}")
else:
    print("Done with total")


numbers = [2, 3, 5]
for number in numbers:
    print(f"Number: {number}")
    if number == 3:
        print(f"Break when {number}")
        break
else:
    print("All numbers are iterated.")


grades = {"John": 90, "Jennifer": 95}
grades["Josh"]

grades.setdefault("Josh", "N/A")

grades.get("Jack", "N/A")

grades

integers = [0, 1, 2, 3, 4, 5, 6]

integers[0:7:2]

integers[::3]

integers[::-1]

integers[0:6:-1]
integers[-1:-7:-1]

integers.reverse()
integers[0:6:1]

from collections import defaultdict

grades = defaultdict(lambda: "N/A", {"John": 90, "Jennifer": 95})
grades["Jack"]
grades
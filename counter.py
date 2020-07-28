scores = ['A', 'B+', 'B', 'C', 'A-', 'B+', 'A']
a_count = scores.count('A')
b_plus_count = scores.count('B+')
f_count = scores.count('F')
print('* A Count:', a_count)
print('* B+ Count:', b_plus_count)
print('* F Count:', f_count)

print('*** Use the count() function with tuples')
grades = ('A', 'B', 'A', 'B', 'A')
for grade in set(grades):
    print(f'{grade} count: {grades.count(grade)}')

print('*** Use the count() function with strings')
word = 'HelloHello'
for letter in set(word):
    print(f'{letter} count: {word.count(letter)}')

from collections import Counter

letters = 'abcabcdaabb'
letter_counter = Counter(letters)
print("Letter Counter:", letter_counter)

letter_counter['a']
letter_counter['c']
letter_counter['z']

nested_lists = [[1, 2, 3], [0, 1, 2], [2, 3, 4]]
unhashable_counter = Counter(nested_lists)


letters = 'xxxxx_yyyy_zzz_aaaaaa_bbbbbb_c'
# Use dictionary comprehension to count each member
letter_counts = {x: letters.count(x) for x in set(letters)}
letter, count = max(letter_counts.items(), key=lambda x: x[1])
print(f"The most frequent letter is {letter} with a count of {count}.")

letter_counter = Counter(letters)
most_freq_letter = letter_counter.most_common(1)
print("Most frequent:", most_freq_letter)

# To find out the most frequent 2 letters
print("Most frequent 2 letters:", letter_counter.most_common(2))
# To find out the most frequent 3 letters
print("Most frequent 3 letters:", letter_counter.most_common(3))

# To find out the least frequent letter
print("Least frequent letter:", letter_counter.most_common()[-1])

letters0 = 'xxxxx_yyyy_zzz_aaaaaa_bbbbbb_c'
letter_counter = Counter(letters0)
print("** Before updating:", letter_counter)
letters1 = 'ddd_llllll'
for letter in letters1:
    letter_counter[letter] += 1
print("** After updating:", letter_counter)

letters2 = "aaaaa_bbbbbbbb"
letter_counter.update(letters2)
print("Letter Counter:", letter_counter)

abc = "aaabbbccc"
amz = "aaaammmmzzzz"
abc_Counter = Counter(abc)
amz_Counter = Counter(amz)
print("abc_Counter:", abc_Counter)
print("amz_Counter:", amz_Counter)

abc_Counter + amz_Counter

abc_Counter - amz_Counter

print("** Before subtraction:", abc_Counter)
abc_Counter.subtract(amz_Counter)
print("** After subtraction:", abc_Counter)

# Create Counter from a mapping
Counter({"a": 5, "b": 4, "c": 3})
# Create Counter from keyword arguments
Counter(x=1, y=2, z=3)

letter_counts = Counter('abbcccdddd')
print("Current Count:", letter_counts)
# Update the a's count
letter_counts['a'] = 10
print("After changing:", letter_counts)
# Remove the b's count
del letter_counts['b']
print("After removing:", letter_counts)

abc_counter = Counter('aabbcc')
acd_counter = Counter('aaaacdddd')
print("Union of Counters:", abc_counter | acd_counter)

print("abc_counter:", abc_counter)
print("acd_counter:", acd_counter)
print("Intersection of Counters:", abc_counter & acd_counter)

# Use the elements() method to get the items with specific counts
item_counter = Counter(a=1, b=2, c=3, x=4, y=5, z=6)
print('_'.join(item_counter.elements()))

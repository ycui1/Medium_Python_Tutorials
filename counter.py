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

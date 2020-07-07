with open('path_to_a_large_file') as file:
    for row in file:
        # do something with each row
        pass


def abc_generator_creator():
    yield 'a'
    yield 'b'
    yield 'c'


abc_gen = abc_generator_creator()
print(type(abc_gen))

for letter in abc_gen:
    print(letter)

abc_gen_expr = (x for x in 'abc')
print(type(abc_gen_expr))

for letter in abc_gen_expr:
    print(letter)

abc_gen_expr = (x for x in 'abc')
len(abc_gen_expr)

integers = [0, 1, 2, 3]
i_integers = iter(integers)
print(type(i_integers))

scores = {'John': 99, 'Danny': 95}
i_scores = iter(scores)
print(type(i_scores))

abc_gen_expr = (x for x in 'abc')
print(next(abc_gen_expr))
print(next(abc_gen_expr))

len(iter(list()))

abc_gen_expr = (x for x in 'abc')
for item in abc_gen_expr:
    print(f'The first iteration: {item}')

print('After the first iteration')
# some other operations

for item in abc_gen_expr:
    print(f'The second iteration: {item}')

print('After the second iteration')

squares_sum = sum(x*x for x in range(1, 5))
print(squares_sum)

squares_list = list(x*x for x in range(1, 5))
print(squares_list)

type(x*x for x in range(1, 5))


def custom_chain(*iterables):
    for iterable in iterables:
        yield from iterable


for x in custom_chain([1, 2, 3], 'abc'):
    print(x, end=' ')


def pool_money(bet, amount):
    while True:
        amount += bet
        bet = yield amount


pool_money_gen = pool_money(0, 100)
print(f'* The beginning: {next(pool_money_gen)}')

# Get the bet from the user, let's assume it's 20 and 50 for two rounds
print(f'* After the second bet of 20: {pool_money_gen.send(20)}')
print(f'* After the third bet of 50: {pool_money_gen.send(50)}')


class TimerFlip(Exception):
    pass


def sand_timer():
    current_level = 100
    while current_level:
        current_level -= 5
        try:
            yield current_level
        except TimerFlip:
            print("Timer will restart.")
            current_level = 100


progress_tracker = sand_timer()
print(next(progress_tracker))
print(next(progress_tracker))
# Flip the sand timer
print(progress_tracker.throw(TimerFlip()))
print(next(progress_tracker))

a = progress_tracker.throw(TimerFlip())

print(a)

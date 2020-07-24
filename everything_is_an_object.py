import sys


class Foo:
    pass


def foo():
    pass


a_tuple = ('Error', 404)
a_dict = {'error_code': 404}
a_list = [1, 2, 3]
a_set = set([2, 3, 5])
objects = [2, 2.2, 'hello', a_tuple, a_dict, a_list, a_set, Foo, foo, sys]

for item in objects:
    print(f'{type(item)} with id: {id(item)}')
i_str = 'Hello'
i_list = [0, 1, 2]
i_tuple = (0, 1)
i_dict = {'zero': 0, 'one': 1}
i_set = {0, 2}
iterables = [i_str, i_list, i_tuple, i_dict, i_set]

for iterable in iterables:
    print("*")
    for item in iterable:
        print(item, end=' ')

>>> import sys
>>> 
>>> class Foo:
...     pass
... 
>>> def foo():
...     pass
... 
>>> a_tuple = ('Error', 404)
>>> a_dict = {'error_code': 404}
>>> a_list = [1, 2, 3]
>>> a_set = set([2, 3, 5])
>>> objects = [2, 2.2, 'hello', a_tuple, a_dict, a_list, a_set, Foo, foo, sys]
>>> 
>>> for item in objects:
...     print(f'{type(item)} with id: {id(item)}')
... 
<class 'int'> with id: 4479354032
<class 'float'> with id: 4481286448
<class 'str'> with id: 4483233904
<class 'tuple'> with id: 4483061152
<class 'dict'> with id: 4483236000
<class 'list'> with id: 4483236720
<class 'set'> with id: 4483128688
<class 'type'> with id: 140235151304256
<class 'function'> with id: 4483031840
<class 'module'> with id: 4480703856

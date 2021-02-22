class Person:
    def speak(self):
        print(f"Speak method is called by {self}")


person0 = Person()
person0.speak()
#
#
# def object_getattribute(obj, name):
#     "Emulate PyObject_GenericGetAttr() in Objects/object.c"
#     null = object()
#     objtype = type(obj)
#     cls_var = getattr(objtype, name, null)
#     descr_get = getattr(type(cls_var), '__get__', null)
#     print("descr_get", descr_get)
#     print("cls_var", cls_var)
#     print("objtype", objtype)
#     if descr_get is not null:
#         if (hasattr(type(cls_var), '__set__') or hasattr(type(cls_var), '__delete__')):
#             print("(hasattr(type(cls_var), '__set__') or hasattr(type(cls_var), '__delete__'))")
#             return descr_get(cls_var, obj, objtype)     # data descriptor
#     if hasattr(obj, '__dict__') and name in vars(obj):
#         print("hasattr(obj, '__dict__') and name in vars(obj)")
#         return vars(obj)[name]                          # instance variable
#     if descr_get is not null:
#         print("descr_get is not null")
#         return descr_get(cls_var, obj, objtype)         # non-data descriptor
#     if cls_var is not null:
#         print("cls_var is not null")
#         return cls_var                                  # class variable
#     raise AttributeError(name)
#
#
# person = Person()
#
# object_getattribute(person, "speak")
#
#
# id(person.speak)
# id(Person.speak)
# id(Person().speak)
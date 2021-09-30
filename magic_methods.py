# Reference: https://dbader.org/blog/python-dunder-methods

class Product:
    def __new__(cls, *args):
        new_product = object.__new__(cls)
        print("Product __new__ gets called")
        return new_product

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("Product __init__ gets called")


product = Product("Vacuum", 150.0)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"

    def __str__(self):
        return f"Product: {self.name}, ${self.price:.2f}"


product = Product("Vacuum", 150.0)
repr(product)
evaluated = eval(repr(product))
type(evaluated)

print(product)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, ${self.price:.2f}"

    def __iter__(self):
        self._free_samples = [Product(self.name, 0) for _ in range(3)]
        print("Iterator of the product is created.")
        return self

    def __next__(self):
        if self._free_samples:
            return self._free_samples.pop()
        else:
            raise StopIteration("All free samples have been dispensed.")


product = Product("Perfume", 5.0)

for i, sample in enumerate(product, 1):
    print(f"Dispense the next sample #{i}: {sample}")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, ${self.price:.2f}"

    def _move_to_center(self):
        print(f"The product ({self}) occupies the center exhibit spot.")

    def _move_to_side(self):
        print(f"Move {self} back.")

    def __enter__(self):
        print("__enter__ is called")
        self._move_to_center()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ is called")
        self._move_to_side()

product = Product("BMW Car", 50000)

with product:
    print("It's a very good car.")



class Product:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == "formatted_name":
            print(f"__getattr__ is called for {item}")
            formatted = self.name.capitalize()
            setattr(self, "formatted_name", formatted)
            return formatted
        else:
            raise AttributeError(f"no attribute of {item}")

    def __setattr__(self, key, value):
        print(f"__setattr__ is called for {key!r}: {value!r}")
        super().__setattr__(key, value)

product = Product("taBLe")
product.name
product.formatted_name
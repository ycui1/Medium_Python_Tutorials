# Create a variable of str type
hello = "Hello Python!"

# Send the data to a function call
print(hello)

# Manipulate the string data with string methods
hello_lower = hello.lower()
hello_upper = hello.upper()
print('lowercased:', hello_lower)
print('uppercased:', hello_upper)

def do_something(item):
    pass

# Repetative work
do_something(item0)
do_something(item1)
do_something(item2)

# Apply DRY
for item in (item0, item1, item3):
    do_something(item)

# install latest version
pip install package_name

# install a particular version
pip install package_name==version_number

# to uninstall a package
pip uninstall package_name

# to show installed packages
pip list

# to show the information about a particular package
pip show package_name

# to install a list of dependencies, such as to clone a virtual environment
pip install -r requirements.txt

class X:
    def bin(self):
        print(f"bin called in X")

class Y(X):
    def go(self):
        print(f"go called Y")

class Z(X):
    def go(self):
        print(f"go called Z")

class W(Y, Z):
    def bin(self):
        super().bin()
        print(f"bin called W")

    def bingo(self):
        self.bin()
        self.go()

w = W()
w.bingo()

print('W Class MRO:', W.__mro__)

class W_(Z, Y):
    pass

print('W_ Class MRO:', W_.__mro__)


def with_EAFP_divide_ten_by(number):
    try:
        print(f'10 divided by {number} is {10 / number}.')
    except ZeroDivisionError:
        print("You can't divide zero.")
    except TypeError:
        print("You can only divide a number.")


def with_LBYL_divide_ten_by(number):
    if isinstance(number, int) or isinstance(number, float):
        if number == 0:
            print("You can't divide zero.")
        else:
            print(f'10 divided by {number} is {10 / number}.')
    else:
        print("You can only divide a number.")


print("Hello World")

3 * 2

>>> print("Hello World!")
Hello World!
>>> 3 * 2
6
>>> type(5)
<class 'int'>
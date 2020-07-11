def calculate_ratio(a, b):
    try:
        print(f"Ratio of {a} and {b} is {a/b}")
    except ZeroDivisionError:
        print("You can't divide zero.")

calculate_ratio(2, 5)
calculate_ratio(2, 0)

def calculate_ratio(a, b):
    print(f"Calculating the ratio between {a!r} and {b!r}")
    try:
        print(f"Ratio of {a} and {b} is {a/b}")
    except:
        print("Something bad just happened.")

calculate_ratio(2, '5')
calculate_ratio(4, 0)

print(2/'a')

def calculate_ratio(a, b):
    print(f"Calculating the ratio between {a!r} and {b!r}")
    try:
        print(f"Ratio of {a} and {b} is {a/b}")
    except TypeError:
        print("Both parameters should be numeric values.")
    except ZeroDivisionError:
        print("You can't divide zero.")

calculate_ratio(2, 5)
calculate_ratio(2, '5')
calculate_ratio(2, 0)

def calculate_ratio(a, b):
    print("Begin calling the function")
    print("Parameter a is:", a)
    print("Parameter b is:", b)
    try:
        print("Ratio: ", a/b)
    except ZeroDivisionError:
        print("You can't divide zero.")

def calculate_ratio(a, b):
    print(f"Calculating the ratio between {a!r} and {b!r}")
    try:
        ratio = a/b
    except ZeroDivisionError:
        print("You can't divide zero.")
    else:
        print("Ratio Result: ", ratio)

calculate_ratio(2, 5)
calculate_ratio(2, 0)

def calculate_ratio(a, b):
    print(f"Calculating the ratio between {a!r} and {b!r}")
    try:
        ratio = a/b
    except ZeroDivisionError:
        print("You can't divide zero.")
    else:
        print("Ratio Result: ", ratio)
    finally:
        print("Done running the calculate_ratio function")

calculate_ratio(2, 5)
calculate_ratio(2, 0)


def calculate_ratio(a, b):
    print(f"Calculating the ratio between {a!r} and {b!r}")
    try:
        ratio = a/b
        return ratio
    except ZeroDivisionError:
        print("You can't divide zero.")
    finally:
        print("Done running the calculate_ratio function")
        return None


calculated_ratio = calculate_ratio(2, 4)
print('Calculated Ratio: ', calculated_ratio)


def calculate_ratio(a, b):
    print(f"Calculating the ratio between {a!r} and {b!r}")
    try:
        casted_a = float(a)
        casted_b = float(b)
        print("Calculated Ratio:", casted_a / casted_b)
    except ZeroDivisionError:
        print("You can't divide zero.")
    except (TypeError, ValueError):
        print("You can only pass numeric values.")

calculate_ratio(2, "4")
calculate_ratio(2, "four")




def simple_generator():
    x = 1
    while x < 4:
        yield x
        x += 1


gen = simple_generator()
for number in gen:
    print(number)


def simple_generator2():
    print("Generator function is called")
    x = 1
    while x < 4:
        print("Before yielding, x value is:", x)
        yield f"yielding: {x}"
        x += 1
        print("After yielding, x value is:", x)

gen2 = simple_generator2()
next(gen2)
next(gen2)
next(gen2)
next(gen2)


def simple_coroutine():
    print("Coroutine just started")
    x = yield "Sending a request"
    print("Coroutine got something back:", x)


coroutine_example = simple_coroutine()
next(coroutine_example)
coroutine_example.send("Here's the data that you requested.")
next(coroutine_example)

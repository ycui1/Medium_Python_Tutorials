clients = list()


def check_in(client):
    clients.append(client)
    print(f"in: New client {client} joined the queue.")


def connect_to_associate(associate):
    if clients:
        client_to_connect = clients.pop(0)
        print(f"out: Remove client {client_to_connect}, connecting to {associate}.")
    else:
        print("No more clients are waiting.")


check_in("John")
check_in("Sam")
connect_to_associate("Emily")
check_in("Danny")
connect_to_associate("Zoe")
connect_to_associate("Jack")
connect_to_associate("Aaron")


from collections import deque
from timeit import timeit


def time_fifo_testing(n):
    integer_l = list(range(n))
    integer_d = deque(range(n))
    t_l = timeit(lambda: integer_l.pop(0), number=n)
    t_d = timeit(lambda: integer_d.popleft(), number=n)
    return f"{n: <9} list: {t_l:.6e} | deque: {t_d:.6e}"


numbers = (100, 1000, 10000, 100000)
for number in numbers:
    print(time_fifo_testing(number))


# 100       list: 2.186300e-05 | deque: 1.461700e-05
# 1000      list: 2.353830e-04 | deque: 1.465280e-04
# 10000     list: 1.561046e-02 | deque: 1.386711e-03
# 100000    list: 1.741322e+00 | deque: 1.344412e-02

from collections import deque

clients = deque()

def check_in(client):
    clients.append(client)
    print(f"in: New client {client} joined the queue.")

def connect_to_associate(associate):
    if clients:
        client_to_connect = clients.popleft()
        print(f"out: Remove client {client_to_connect}, connecting to {associate}.")
    else:
        print("No more clients are waiting.")

from time import time
from time import sleep


def totaltime(func):
    def start(*args, **kwargs):
        k1 = time()
        func(*args, **kwargs)
        k2 = time()
        print("total time", k2 - k1)

    return start


@totaltime
def sum(x, y):
    print(x + y)
    sleep(1)


a = float(input())
b = float(input())

sum(a, b)

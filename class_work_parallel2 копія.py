from threading import Thread
import time

import logging


logging.basicConfig(level=logging.DEBUG)

def fib(n:int) ->int:
    global T
    a, b = 1, 1
    for _ in range(n):
        a , b = a+b, a
    T = a
    logging.debug(f"T={T}")
    return a

n = 20

th1 = Thread(target=fib, args = (n,))
th1.start()
th1.join()

print (f"T={T}")

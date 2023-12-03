import threading
import time

import logging

class TreadReturning(threading.Thread):

    def __init__(self,fun,args=()):
        threading.Thread.__init__(self)
        self.result = None
        self._fun = fun
        self._args = args
        self._exept = None
    def run(self):
        try:
            self.result = self._fun(*self._args)
        except ValueError as e:
            self._exept = e


    def getResult(self):
        return self.result

    def getExcept(self):
        return self._exept


logging.basicConfig(level=logging.DEBUG)
def factorial1(n:int) ->int:
    logging.debug("Обчислення рекурсивного факторіалу для {}".format(n))

    try:
        m = int(n)
    except ValueError as e:
        raise e

    if n <=1:
        return 1
    r = n * factorial1(n-1)
    logging.debug("Result {}".format(r))
    return r

def factorial2(n:int) ->int:
    logging.debug("Обчислення факторіалу циклами для {}".format(n))
    p = 1
    for i in range(1,n-1):
        logging.debug("Обчислення факторіалу циклами для {}".format(i))
        p *= i
    logging.debug("Result {}".format(p))
    return p

n = 20


#threed1 = threading.Thread(target=factorial1,args=(n,))
#threed2 = threading.Thread(target=factorial2,args=(n,))
thread1 = TreadReturning(factorial1, args=(n,))
thread2 = TreadReturning(factorial2, args=(n,))



thread1.start()
thread2.start()

thread1.join()
thread2.join()

if thread1.getExcept():
    print ("виключення в потоці 1")
    print (thread1.getExcept())
else:
    print ("без виключень")
    print (thread1.getResult())

if thread2.getExcept():
    print ("виключення в потоці 1")
    print (thread1.getExcept())
else:
    print ("без виключень")
    print (thread1.getResult())


print("B t w f")




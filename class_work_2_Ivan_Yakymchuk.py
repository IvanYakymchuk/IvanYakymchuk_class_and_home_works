import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd


@np.vectorize
def func01(n):
    return 3 / 2 * (1 - 1/pow(3, n+1)) * (n - 3) * pow(n, 1/n) / (2.0 * n + 5 / n)


def gety(f, x):
    """ Повертає масив значень функції f(x) (альтернатва векторизації)"""
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    return y


def plot_seq(x, y, b=None, eps=0.01, forall=True):
    """ Візуалізує послідовність y = f(x)"""
    plt.figure(figsize=(12, 9))
    if b is None:

        plt.plot(x, y, ".b")
        return x[-1], y[-1]
    else:



        k = -1

        prev = False

        for i in range(y.size):
            if abs(y[i] - b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False


        if not prev:
            return None, None


        begin = 0 if forall else k


        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")

        plt.xlabel("n")
        plt.ylabel("a(n)")
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])
        return x[k], y[k]

def func20_1():
    t = (1, 2000, 1)
    x = np.arange(*t)
    y = func01(x)

    b = 0.75
    eps = 0.01
    x0, y0 = plot_seq(x, y, b, eps, True)
    print(x0, y0)
    plt.show()

def func20_8():
    ar = np.array([int(x) for x in input("Введіть елементи ").split()])
    ar1 = ar[ar < 0]
    ar2 = ar[ar >= 0]
    ar3 = np.concatenate((ar1,ar2))
    print (ar3)

def func20_2():
    N = int(input("введіть кількість точок"))
    x = rnd.uniform(-1, 1, N)
    y = rnd.uniform(0, 1, N)

    z = x**2 + y**2
    inside = z[z <= 1]

    L = len(inside)
    our_pi = 4*L/N
    print(f"pi = {our_pi}, error = {np.pi - our_pi }")

    X = np.linspace(-1, 1, 100)
    Y = np.sqrt(1 - np.power(X,2))
    plt.plot(X,Y)
    plt.plot(X, np.zeros_like(X))
    plt.plot(X, np.ones_like(X))
    plt.plot(-np.ones(100), np.linspace(0, 1, 100))
    plt.plot(np.ones(100), np.linspace(0, 1, 100))

    plt.scatter(x,y)

    plt.show()

def main():
    while True:
        print("\nОберіть завдання:")
        print("\n1. завдання 20_1(a)")
        print("\n2. завдання 20_2")
        print("\n8. завдання 20_8")
        print("\nДля завершення програми напишіть 'end' ")


        number_of_task = input("\nВведіть номер завдання (або 0 для виходу): ")


        if number_of_task == '1':
            func20_1()
        elif number_of_task == '2':
            func20_2()
        elif number_of_task == '8':
            func20_8()
        elif number_of_task == 'end':
            break
        else:
            print("Завдання з таким номером не існує")
if __name__ == "__main__":

    main()
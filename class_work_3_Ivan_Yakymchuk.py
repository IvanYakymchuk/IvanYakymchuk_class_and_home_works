import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd


def func20_17(N):
    x = rnd.uniform(-1, 1, N)
    y = rnd.uniform(0, 1, N)

    z = x ** 2 + y ** 2
    inside = z[z <= 1]

    L = len(inside)
    our_pi = 4 * L / N
    print(f"pi = {our_pi}, error = {np.pi - our_pi}")

    X = np.linspace(-1, 1, 100)
    Y = np.sqrt(1 - np.power(X, 2))
    plt.plot(X, Y)
    plt.plot(X, np.zeros_like(X))
    plt.plot(X, np.ones_like(X))
    plt.plot(-np.ones(100), np.linspace(0, 1, 100))
    plt.plot(np.ones(100), np.linspace(0, 1, 100))

    plt.scatter(x, y)

    plt.show()

def func20_23():
    n = 100
    A = np.arange(0, 12 * n, dtype=int)
    A.shape = (12, n)
    print(A)
    S = 0
    for i in range(n):
        B = rnd.choice(A[:, i], 3, replace=False)
        C = B[B % 3 == 0]
        S += (len(C) >= 2)
    print(f"Probability -{S / n:.02}")
if __name__ == "__main__":

    func20_17(100)
    func20_23()

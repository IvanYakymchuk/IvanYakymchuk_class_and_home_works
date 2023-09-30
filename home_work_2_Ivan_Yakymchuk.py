import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd


@np.vectorize
def func01(n):
    return (np.power(n - 1,4) - np.power(n + 2,4))/(np.power(2*n + 1, 3) + np.power(n-1, 3))



def plot_seq(x, y, b=None, eps=0.01, forall=True):
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


if __name__ == "__main__":
    t = (1, 1000, 1)
    x = np.arange(*t)
    y = func01(x)
    b = -1.333333333  # границя
    eps = 0.01
    x0, y0 = plot_seq(x, y, b, eps, True)
    print(x0, y0)
    plt.show()
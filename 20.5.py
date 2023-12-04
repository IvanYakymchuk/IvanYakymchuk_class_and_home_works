import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):
    result = 0
    for i in range(len(y_values)):
        block = y_values[i]
        for j in range(len(x_values)):
            if j != i:
                block = block * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += block
    return result

def graphic_interpolation(k):
    n = 2**k
    x_interp = np.linspace(0, 2 * np.pi, 1000)
    y_sin = np.sin(x_interp)

    x_values = np.linspace(0, 2 * np.pi, n + 1)
    y_values = np.sin(x_values)

    y_interp = [lagrange_interpolation(x_values, y_values, x) for x in x_interp]

    plt.plot(x_interp, y_sin, label='sin(x)', color='blue')
    plt.plot(x_interp, y_interp, label=f'P(x)', color='red', linestyle='dashed')
    plt.scatter(x_values, y_values, color='black', marker='o')

    plt.title(f'Інтерполяція sin(x) за допомогою поліному Лагранжа, для k = {k}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


k_value = 2


graphic_interpolation(k_value)

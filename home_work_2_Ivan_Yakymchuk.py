import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


@np.vectorize
def func20_2(n):
    return (n * np.sin(np.radians(360 / n))) / (2 * np.cos(np.radians(180 / n)))


def update(frame):
    plt.clf()
    n = v[frame]
    radius = 1
    angle = 2 * np.pi / n
    x_points = [radius * np.cos(i * angle) for i in range(n + 1)]
    y_points = [radius * np.sin(i * angle) for i in range(n + 1)]
    x_points.append(x_points[0])
    y_points.append(y_points[0])

    circle = plt.Circle((0, 0), radius, fill=False, color='b', linewidth=2)
    plt.gca().add_patch(circle)

    plt.plot(x_points, y_points, marker='o', linestyle='-', color='r', markersize=8)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Вписаний {n}-кутник у коло")


def main(k):
    global v
    v = np.power(2, np.arange(2,k+1))

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update, frames=len(v), interval=1000, repeat=False)
    plt.show()


if __name__ == "__main__":
    main(10)

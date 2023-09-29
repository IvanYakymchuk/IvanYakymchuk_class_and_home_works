import numpy as np
import matplotlib.pyplot as plt
import random


def task_1():
    X = np.random.random_sample((1, 25))
    X = X.reshape((5,5))
    min = X.min()
    max = X.max()
    normalized_X = (X - min) / (max - min)
    print (normalized_X)


def task_2():
    ar1 = np.array([int(x) for x in input("Введіть елементи ").split()])
    ar2 = np.array([int(x) for x in input("Введіть елементи ").split()])
    com_el = np.intersect1d(ar1,ar2)
    print(f"спільні елементи вищевведених масивів: {com_el}")

def task_3():
    Y = np.random.random_sample((1, 25))
    Y = Y.reshape((5,5))
    i = 0
    while i < 5:
        Y[i, :] = i
        i+=1
    print(Y)


def task_4():
    a, b = [int(x) for x in input("введіть нижню і верхню межі діапазону випадуових цілих чисел: ").split()]
    random_array = np.random.randint(a, b, 10)

    print (random_array)


def task_5():
    random_array = np.random.rand(10)
    random_array.sort()
    print(random_array)

def task_6():
    r1 = np.random.rand(random.randrange(1, 10))
    r2 = np.random.rand(random.randrange(1, 10))
    if np.array_equal(r1, r2):
        print("випадкові масиви рівні")
        print(r1)
        print(r2)
    else:
        print("випадкові масиви не рівні")
        print(r1)
        print(r2)

def main():
    while True:
        print("\nОберіть завдання:")
        print("\n2. Нормалізуйте випадкову матрицю 5x5")
        print("\n3. Знайти спільні значення між двома масивами?")
        print("\n4. Створіть матрицю 5x5 зі значеннями рядків від 0 до 4")
        print("\n5. Створить функцію-генератор, яка генерує 10 цілих чисел, і використовуйте її для створення масиву")
        print("\n6. Створіть випадковий вектор розміром 10 і відсортуйте його")
        print("\n7. Розгляньте два випадкових масиви A і B, перевірте, чи вони рівні")
        print("\nДля завершення програми напишіть 'end' ")


        number_of_task = input("Введіть номер завдання (або 0 для виходу): ")


        if number_of_task == '2':
            task_1()
        elif number_of_task == '3':
            task_2()
        elif number_of_task == '4':
            task_3()
        elif number_of_task == '5':
            task_4()
        elif number_of_task == '6':
            task_5()
        elif number_of_task == '7':
            task_6()
        elif number_of_task == 'end':
            break
        else:
            print("Завдання з таким номером не існує")

if __name__ == "__main__":

    main()




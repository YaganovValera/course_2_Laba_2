"""
Лабораторная работа №2, Вариант: 27

Задание: Вычислить сумму знакопеременного ряда |х*(3n-1)| / (3n-1)!, где х-матрица размера к (к и матрица задаются случайным образом),
n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность. Операция умножения –поэлементная.

Выполнил: Яганов Валерий ИСТбд-21
"""

import numpy as np

def factorial(current_fact, fact):
    if fact != 2:
        new_fact = current_fact * (fact - 2) * (fact - 1) * fact
    else:
        return 2
    return new_fact


def algorithm(n, current_fact, det_matrix, matrix_size):
    fact = 3 * n - 1
    current_fact = factorial(current_fact, fact)                                                                            # Вычисление факториала
    det_matrix = det_matrix * (fact)**matrix_size                                                                           # Поиск определителя
    current_cal = det_matrix / current_fact * (-1)**n                                                                       # текущее вычисление
    return current_cal, current_fact

try:
    while True:                                                                                                                         # Получени данных
        matrix_size = input("Введите длину матрицы (положительное, целое число, в диапазоне от 3 до 50): ")
        accuracy = input("Введите точность вычисления (кол-во знаков после запятой, в диапозоне от 1 до 20): ")
        matrix_size = matrix_size.strip()
        accuracy = accuracy.strip()
        if matrix_size.isdigit() and accuracy.isdigit():
            matrix_size = int(matrix_size)
            accuracy = int(accuracy)
            if (matrix_size >= 3) and (matrix_size <= 50) and (accuracy <= 20) and (accuracy >= 1):
                break
            else:
                print("Ошибка. Заданное число не входит в разрешенный диапазон.")
        else:
            print("Неверный ввод данных.")

    n = 1
    current_fact = 1
    sum_row = 0
    while True:
        # matrix = np.array([                                                                                                 # Матрица для проверки
        #     [1, 2, 32, 42, -35],
        #     [23, 4, 3, -45, -3],
        #     [-4, -3, 34, 43, 4],
        #     [3, 2, -5, -5, 4],
        #     [-45, 3, 2, 32, -3]
        # ])
        matrix = np.random.randint(-10, 11, size=(matrix_size, matrix_size))                                                    # Создание матрицы
        det_matrix = np.linalg.det(matrix)                                                                                      # Поиск определителя
        if det_matrix == 0:
            continue
        break

    while True:
        current_cal, current_fact = algorithm(n, current_fact, det_matrix, matrix_size)
        sum_row += current_cal
        n += 1
        if abs(current_cal) <= 10**(-accuracy):
            print("Сумма знакопеременного ряда равна с точностью {0}, после запятой: {1:.21f}".format(accuracy, sum_row))
            break
except:
    print("Извините, произошла ошибка.")


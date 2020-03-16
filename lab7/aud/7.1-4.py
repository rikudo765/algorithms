"""
Реалізуйте підпрограми сортування масиву.
"""


def bubble_sort(array):
    """ Сортування "Бульбашкою"
    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        check = True
        for j in range(i):
            if array[j] > array[j + 1]:
                check = False
                array[j], array[j + 1] = array[j + 1], array[j]
        if check:
            break


def selection_sort(array):
    """ Сортування вибором
    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        m = 0
        for j in range(1, i + 1):
            if array[m] < array[j]:
                m = j
        array[i], array[m] = array[m], array[i]


def insertion_sort(array):
    """ Сортування вставкою
    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(1, n):
        cur = array[i]
        pos = i
        while pos > 0:
            if array[pos - 1] > cur:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1
        array[pos] = cur

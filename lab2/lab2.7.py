def bsearch_leftmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        else:
            right = m
    return left


def bsearch_rightmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] <= x:
            left = m + 1
        else:
            right = m
    return left - 1


def counter(array, x):
    left = bsearch_leftmost(array, x)
    right = bsearch_rightmost(array, x)
    res = right - left + 1
    return res


lst = [10, 10, 33, 33, 33, 44, 55, 66]
print(counter(lst, 33))

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


lst = [11, 11, 22, 33, 44]
print(bsearch_rightmost(lst, 11))

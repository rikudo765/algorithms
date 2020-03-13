def binary_search(lst, x):
    if len(lst) == 0:
        return False
    else:
        m = len(lst) // 2
        if lst[m] == x:
            return True
        else:
            if x < lst[m]:
                return binary_search(lst[:m], x)
            else:
                return binary_search(lst[m + 1:], x)


lst = [1, 2, 3, 4, 7, 8, 11, 44, 32, 64]
print(binary_search(lst, 3))
print(binary_search(lst, 33))

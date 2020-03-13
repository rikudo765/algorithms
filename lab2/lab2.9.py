def search(lst, x):
    left = 0
    right = len(lst) - 1
    while (x <= lst[right]) and (lst[left] <= x):
        if lst[right] <= x:
            return right
        elif x <= lst[left]:
            return left
        else:
            left += 1
            right -= 1
    return None


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search(lst, 10))

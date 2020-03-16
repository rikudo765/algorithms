n = int(input())
lst = list(map(int, input().split()))


def sort(arr):
    l = len(arr)
    k = 0
    for i in range(l - 1, 0, -1):
        check = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                check = True
                k += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not check:
            return k
    return k


print(sort(lst))

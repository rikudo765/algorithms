n = int(input())
lst = list(map(int, input().split()))


def sort1(arr):
    l = len(arr)
    
    for i in range(1, n):
        cur = arr[i]
        pos = i
        check = False
        while pos > 0:
            if arr[pos - 1] > cur:
                check = True
                arr[pos] = arr[pos - 1]
            else:
                break
            pos -= 1
        arr[pos] = cur
        if check:
            for j in range(len(arr)):
                print(arr[j], end=' ')
            print('')


sort1(lst)

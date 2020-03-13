from math import log


def checker(n):
    ln = log(n, 2)
    if ln == int(ln):
        return True

    return False


lst = [1, 2, 3, 4, 7, 8, 11, 44, 32, 64]
result = dict()

for i, e in enumerate(lst):
    if checker(e):
        result[e] = i

print(result)

from math import sin


def binary_continuous(f, c, a, b):
    left = a
    right = b
    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) <= c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return left


def function(x):
    return x ** 3 + x + 1


def func2(x):
    return x / sin(x)


def func3(x):
    return x ** 3 + 4 * x ** 2 + x - 6


print(binary_continuous(function, 5, 0, 10))
print(binary_continuous(func2, 3, 1.6, 3))
print(binary_continuous(func3, 0, 0, 2))

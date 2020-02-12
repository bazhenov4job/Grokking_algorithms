"""Алгоритм нахождения суммы элементов массива при помощи рекурсии"""
import random

list = [random.randint(0, 10) for _ in range(10)]
print(list)


def summa(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + summa(list[1:])


print(sum(list))
print(summa(list))

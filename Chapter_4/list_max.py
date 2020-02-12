"""Рекурсивнная функция поиска наибольшего числа в списке"""
import random

list = [random.randint(0, 20) for _ in range(10)]
print(list)


def maximum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] if list[0] > maximum(list[1:]) else maximum(list[1:])


print(max(list))
print(maximum(list))

"""Рекурсивная функция для подсчёта элеметов в списке"""
import random


list = [_ for _ in range(random.randint(20, 40))]
print(list)


def length(list, depth=0):
    try:
        list.pop()
        depth += 1
        return length(list, depth)
    except IndexError:
        return depth


print(length(list))

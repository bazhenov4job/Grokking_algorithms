"""Алгоритм сортировки выбором"""
import random


list = [random.randint(0, 100) for i in range(10)]
print(list)


def choise_sort(list):

    i_min = 0
    length = len(list)

    for i in range(length):
        lowest = list[i]
        for j in range(i, length):
            if list[j] < lowest:
                lowest = list[j]
                i_min = j
        list[i], list[i_min] = list[i_min], list[i]

    return list


print(choise_sort(list))

"""Алгоритм бинарного поиска"""
import random


list = [i for i in range(0, 10000000, 1)]
item = int(input("Enter number to find: "))


def binary_search(list, item):
    #Function returns required element's position

    i = 0
    start = 0
    finish = len(list) - 1

    while start <= finish:
        i += 1
        mid = (start + finish) // 2
        guess = list[mid]
        print(i, guess)
        if item == guess:
            return mid
        elif guess > item:
            finish = mid - 1
        else:
            start = mid + 1
    else:
        return "no element in list"


print(binary_search(list, item))

"""Реализация бинарного поиска рекурсией"""
import random


list = [random.randint(0, 100) for _ in range(15)]
list.sort()
item = random.choice(list)
print(list)
print(item)


def binary_recursion(list, item, position):
    middle = len(list) // 2
    element = list[middle]

    if element != item:
        if item > element:
            position += 1 + len(list[middle + 1:]) // 2
            return binary_recursion(list[middle + 1:], item, position)
        else:
            position -= 1 + len(list[:middle]) // 2
            return binary_recursion(list[:middle], item, position)

    else:
        return position


print(binary_recursion(list, item, len(list) // 2))

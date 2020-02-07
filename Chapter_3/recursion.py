"""Задача с рекурсией номер 1"""
"""Обратный отсчёт"""

n = 5


def countdown(n):
    print(n)
    if n <= 1:
        return n
    else:
        countdown(n-1)


countdown(n)


"""Задача N2, вычисление факториала"""


def factorial(n):
    if n == 1:
        return n

    else:
        return n * factorial(n-1)


print(factorial(n))

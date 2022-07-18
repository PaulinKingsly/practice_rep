"""Модуль 3 Часть 1 Задание 1"""
x = int(input('Сумма вклада: '))
p = int(input('Процент годовых: '))
y = int(input('Сумма вклада через некоторое кол-во лет: '))
c = 0
while x < y:
    x = x + (x * (p / 100))
    c += 1
print(c)

# """Модуль 3 Часть 1 Задание 2"""
n = int(input(""))
while n > 0:
        for i in range(n):
            print('For - частный случай цикла while')
            n -= 1


# """Модуль 3 Часть 1 Задание 3"""

num = int(input("Введите целое число: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)
 """Модуль 3 Часть 3 Задание 1"""

'''В этой части все задания не смогла доделать. В чем ошибки?'''
import math
a = float(input(''))
b = float(input(''))
c = float(input(''))

def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a)*(p - b)*(p - c)) ** 0.5
    print(s)

area(a, b, c)



"""Модуль 3 Часть 3 Задание 2"""

s = '''Было просто пасмурно, дуло с севера,
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого,
То ли весь мир сошёл с ума, то ли я - того.
На столе записка от неё смятая,
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу,
Первое сентября, дворник жжёт листву.
И серым облакам наплевать на нас,
Если знаешь, как жить - живи
Ты хотела плыть, как все?
Так плыви...'''
words = s.split()
list = []
def function():
    for word in words:
        if len(word) < 5:
             list.append(word)
    print(list)
function()

"""Модуль 3 Часть 3 Задание 3"""

num = [56, 9, 11, 2]
max_num = []
def sum():
    while len(num) > 0:
        max_number = max(num)
        max_num.append(max_number)
        num.remove(max_number)
    print("".join(map(str, max_num)))
sum()
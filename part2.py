"""Модуль 3 Часть 2 Задание 1"""

l = [5, 6, 5, 'hello', 4, 5, 2, 1, 3, 1, 'hello']
list = []

for i in l:
    if l.count(i) >= 2:
        list.append(i)
print(list)

"""Модуль 3 Часть 2 Задание 3"""

dict = {'Ann': 25, 'Alex': 30, 'Polina': 19}
new_dict = {}
for k, v in dict.items():
    new_dict[v] = k
print(new_dict)
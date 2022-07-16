"""Модуль 3 Часть 4 Задание 1"""
import json

data = {'login': input('Login: '), 'password': input('Password: ')}

with open('reg.json', 'w') as f:
     json.dump(data, f)

'''Без функции все работает. Добавляю функцию без аргументов: '''

def registration():
    with open('reg.json', 'w') as f:
        return json.dump(data, f)
registration()

'''Тоже работает. Добавляю аргументы в функцию: '''

import json

data = {'login': input('Login: '), 'password': input('Password: ')}

def registration(login, password):
    with open('reg.json', 'w') as f:
        return json.dump(data, f)
registration()

'''Ошибка: TypeError: registration() missing 2 required positional arguments: 'login' and 'password' Нужно написать два аргумента:
логин и пароль. Но логин и пароль должны быть взяты из второй строчки кода (пользователь сам их вводит). В чем здесь ошибка?'''
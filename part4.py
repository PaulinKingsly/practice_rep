"""Модуль 3 Часть 4 Задание 1"""
import json

data = {'login': input('Login: '), 'password': input('Password: ')}

def registration():
    with open('reg.json', 'w') as f:
        return json.dump(data, f)
registration()
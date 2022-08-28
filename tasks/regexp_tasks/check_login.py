"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""


import re


def check_login(login_string: str):
    pattern = re.compile(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[_])(?:.{5,20})')
    if not pattern.match(login_string):
        return False
    else:
        return True

"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""


import re


def count_words(string: str):
    count_words_val = len(re.findall(r'\w+', string))
    return count_words_val

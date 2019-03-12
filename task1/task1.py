# Task1: Посчитать сколько раз в файле встречается символ.

import os


def find_one_char(char, pth):

    if os.path.isfile(pth) and os.access(pth, os.R_OK):
        while True:
            if len(char) != 1:
                print('Введите ровно один символ')
            else:
                with open('task1_data.txt', 'rb') as f:
                    content = f.read()
                    return print('Символ \'{}\' встечается в тексте {} раз'.format(char, content.count(char.encode('utf-8'))))
    else:
        print('Файл не существует или не доступен для чтения')


if __name__ == "__main__":
    char = input('Введите один символ для поиска в тексте: ')
    pth = 'task1_data.txt'
    find_one_char(char, pth)


# Результат:
# $ python3 task1.py
# Введите один символ для поиска в тексте: а
# Символ 'а' встечается в тексте 119 раз

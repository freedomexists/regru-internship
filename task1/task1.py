# Task1: Посчитать сколько раз в файле встречается символ.


def find_one_char(char):
    while True:
        if len(char) != 1:
            print('Введите ровно один символ')
        else:
            with open('task1_data.txt', 'rb+') as f:
                content = f.read()
                return content.count(char.encode('utf-8'))


if __name__ == "__main__":
    char = input('Введите один символ для поиска в тексте: ')
    print('Символ \'{}\' встечается в тексте {} раз'.format(char, find_one_char(char)))


# Результат:
# $ python3 task1.py
# Введите один символ для поиска в тексте: а
# Символ 'а' встечается в тексте 119 раз

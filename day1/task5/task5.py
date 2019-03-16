# Task5: Прочитать содержимое файла task5_data.txt в простом режиме и вывести.
# Прочитать каждый симбол в бинарном режиме и заменить второй# младший бит
# у каждого байта на противоположный. Полученные данные записать
# в бинарном режиме в файл 'task5_data_new.txt'.
# Вывести содержимое файла в обычном режиме.

import os

if __name__ == '__main__':

    pth = 'task5_data.txt'

    if os.path.isfile(pth):

        with open(pth, 'r') as f:
            print(f.read())

        if os.access(os.path.split(os.path.abspath(pth))[1], os.X_OK):

            with open(pth, 'rb') as f, open('task5_data_new.txt', 'wb+') as new:
                char = f.read(1)
                i = 1

                while char:
                    new.write(bytes([ord(char) ^ 0b000010]))
                    char = f.read(1)
                    i = i + 1
        else:
            print('Ошибка. Не достаточно прав.')

        with open('task5_data_new.txt', 'r') as f:
            print(f.read())

    else:
        print('Ошибка. Указанный путь не является файлом или не существует.')

# Результат:
# $ python3 task5.py
# 12йцas
# 30һӄcq

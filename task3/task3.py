# Программа принимает на вход строку. Эта строка — путь к файлу.
# В случае существования файла:
# 1) проверить возможна ли в него запись.
# 2) удалить, и закончить работу.
# Если файла нет:
# 1) создать,
# 2) записать строку c латинскими и кириллическими буквами в кодировке UTF-8
# 3) прочитать и вывести содержимое в кодировке WINDOWS-1251 и в кодировке UTF-8
# 4) удалить, и закончить работу.


import sys
import os


if __name__ == '__main__':

    try:
        pth = sys.argv[1]
        if os.path.isfile(pth):
            print('Доступ на запись - {}'.format(os.access(pth, os.R_OK)))
            os.remove(pth)

        else:

            try:
                with open(pth, 'wb+') as f:
                    f.write('some string строка'.encode('utf-8'))
                    f.seek(0)
                    content = f.read()
                    print(content.decode('WINDOWS-1251'), content.decode('utf-8'), sep='\n')
                if os.access(os.path.dirname(pth), os.X_OK) or not os.path.dirname(pth):
                    os.remove(pth)
                else:
                    print('Не достаточно прав для удаления файла')

            except IsADirectoryError:
                print('Ожидается файл, указана директория')

    except IndexError:
        print('Введите путь до файла в качестве параметра')


# $ sudo python3 task3.py /home/test.txt
# some string СЃС‚СЂРѕРєР°
# some string строка

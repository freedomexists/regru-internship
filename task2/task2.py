# Task2: Дописать содержимое второго файла к первому,
# предварительно сделав 3 перевода строки.
# Переименовать первый файл. 'task2_data_all.txt'
# Удалить второй файл.


import os

if __name__ == '__main__':
    pth_f1 = 'task2_data_1.txt'
    pth_f2 = 'task2_data_2.txt'

    if os.path.isfile(pth_f1) and os.path.isfile(pth_f2) and os.access(pth_f1, os.W_OK) and os.access(pth_f2, os.R_OK):

        with open(pth_f1, 'ab') as f1:
            f1.write('\n\n\n'.encode('utf-8'))

            with open(pth_f2, 'rb') as f2:
                for line in f2.readlines():
                    f1.write(line)

        os.rename(pth_f1, 'task2_data_all.txt')
        os.remove(pth_f2)

    else:
        print('Ошибка. Проверьте существование файлов и права доступа к ним.')

# Результат:
# $ ls
# task2_data_1.txt  task2_data_2.txt  task2.py
# $ cat task2_data_1.txt
# 1 2 3 4 5 6
# $ cat task2_data_2.txt
# 11 22 33
# 44 55 66
# $ python3 task2.py
# task2_data_all.txt  task2.py
# $ python3 task2.py
# $ ls
# task2_data_all.txt  task2.py
# $ cat task2_data_all.txt
# 1 2 3 4 5 6
#
#
#
# 11 22 33
# 44 55 66

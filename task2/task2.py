# Task2: Дописать содержимое второго файла к первому,
# предварительно сделав 3 перевода строки.
# Переименовать первый файл. 'task2_data_all.txt'
# Удалить второй файл.


import os

if __name__ == '__main__':
    with open('task2_data_1.txt', 'ab') as f1:
        f1.write('\n\n\n'.encode('utf-8'))
        with open('task2_data_2.txt', 'rb') as f2:
            for line in f2.readlines():
                f1.write(line)
    os.rename('task2_data_1.txt', 'task2_data_all.txt')
    os.remove('task2_data_2.txt')

# Результат:

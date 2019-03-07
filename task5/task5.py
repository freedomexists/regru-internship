# Task5: Прочитать содержимое файла task5_data.txt в простом режиме и вывести.
# Прочитать каждый симбол в бинарном режиме и заменить второй# младший бит
# у каждого байта на противоположный. Полученные данные записать
# в бинарном режиме в файл 'task5_data_new.txt'.
# Вывести содержимое файла в обычном режиме.


if __name__ == '__main__':

    with open('task5_data.txt', 'r') as f:
        print(f.read())

    with open('task5_data.txt', 'rb') as f, open('task5_data_new.txt', 'wb+') as new:
        b_array = bytearray()
        text = f.read(1)
        i = 1
        while text:
            b_array.append(int(text.hex(), 16) ^ 0b000010)
            text = f.read(1)
            i = i + 1
        new.write(b_array)

    with open('task5_data_new.txt', 'r') as f:
        print(f.read())


# Результат:
# $ python3 task5.py
# 12йцas
# 30һӄcq

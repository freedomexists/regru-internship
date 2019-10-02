# task2:
# Создать функцию, которая принимает размер N матрицы, и номер строки M этой матрицы.
# Функция должна вывести последовательность числел, которые находятся в строке с номером M в спиральной матрице
# (по аналогии с первой задачей). Нужно это сделать без просчета всей матрицы
# (вообще ничего нельзя просчитывать кроме этой строки).


def w_func(n, i, j):

    if j == 0:
        return 4 * (n - 1) - i + 1
    else:
        return 4 * (n - 2 * j - 1) + 1 + w_func(n, i, j - 1)


def e_func(n, i, j):

    if j == 0:
        return n + i
    else:
        return 4 * (n - 2 * j) + 1 + e_func(n, i, j - 1)


try:
    n = int(input('Введите размер матрицы: '))
    m = int(input('Введите номер строки: '))

except ValueError:
    print('Ошибка. Введите число')

else:

    align = len(str(n * n))
    line = []
    i = m - 1

    if i <= n // 2:

        for j in range(i):
            line.append(w_func(n, i, j))

        for j in range(n - 2 * i):
            line.append(4 * (n - i) * i + j + 1)

        for j in range(i - 1, -1, -1):
            line.append(e_func(n, i, j))

    else:

        for j in range(n - i - 1):
            line.append(w_func(n, i, j))

        for j in range(n - (n - i - 1) * 2, 0, -1):
            line.append(4 * i * (n - i - 1) + 2 * n - 2 + j)

        for j in range(n-i-2, -1, -1):
            line.append(e_func(n, i, j))

    print(' '.join(['{:>{}}'.format(line[i], align) for i in range(n)]))

# Результат:
# $ python3 task2.py
# Введите размер матрицы: 10
# Введите номер строки: 7
#  31  60  81  94  93  92  91  74  49  16

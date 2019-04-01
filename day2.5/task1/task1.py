# task1:
# Задача № 1
# Нужно создать матрицу, NxN, и заполнить ее натуральными числами от 1 до NxN по спирали во внутрь по часовой стрелке.
# Результат вывести в виде квадратной матрицы.


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


n = int(input('Введите размер матрицы: '))
align = len(str(n * n))

for i in range(n):

    line = []

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
# $ python3 task1.py
# $ python3 task1.py
# Введите размер матрицы: 10
#   1   2   3   4   5   6   7   8   9  10
#  36  37  38  39  40  41  42  43  44  11
#  35  64  65  66  67  68  69  70  45  12
#  34  63  84  85  86  87  88  71  46  13
#  33  62  83  96  97  98  89  72  47  14
#  32  61  82  95 100  99  90  73  48  15
#  31  60  81  94  93  92  91  74  49  16
#  30  59  80  79  78  77  76  75  50  17
#  29  58  57  56  55  54  53  52  51  18
#  28  27  26  25  24  23  22  21  20  19



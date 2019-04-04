# task1:
# Задача № 1
# Нужно создать матрицу, NxN, и заполнить ее натуральными числами от 1 до NxN по спирали во внутрь по часовой стрелке.
# Результат вывести в виде квадратной матрицы.

try:
    n = int(input('Введите размер матрицы: '))

except ValueError:
    print('Ошибка. Введите число')

else:
    max_num = n * n
    align = len(str(max_num))
    i = 0
    j = 0
    num = 1
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    while num <= max_num:

        matrix[i][j] = num

        if i <= j + 1 and i + j < n - 1:
            j += 1

        elif i < j and i + j >= n - 1:
            i += 1

        elif i >= j and i + j > n - 1:
            j -= 1

        else:
            i -= 1

        num += 1

    print('\n'.join([' '.join('{:>{}}'.format(matrix[i][j], align) for j in range(n)) for i in range(n)]))

# Результат:
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



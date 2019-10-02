# Task2:
# Напишите программу, которая использует список из задачи 1, и складывает все численные данные.
# Постарайтесь использовать максимально возможное кол-во элементов.

lst = [1, 5445, 5445.0, 1.56, '1.90', 'сорок_два', False, '', True]
summ = 0

for elem in lst:

    try:
        summ += float(elem)
    except ValueError:
        pass

print(summ)

# В одну строку, но, вроде, не читабельно.
# print(sum(elem if isinstance(elem, (int, float))
#           else float(elem) if isinstance(elem, str) and is_float(elem) else 0 for elem in lst))


# $ python3 task2.py
# 10895.46

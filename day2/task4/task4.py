# task4:
# Напишите программу, которая принимает строку в формате «php=Rasmus Lerdorf; perl=Larry Wall;
# python=Guido van Rossum». Постройте словарь, где ключи — значения слева от «=»,
# а значения — справа от «=». Разделитель — «;». Инвертируйте словарь так,
# чтобы значения стали ключами, а ключи — значениями. Выведите получившиеся словари
# в отсортированном по ключам виде, разделённые 40 решётками.
# Гарантируется, что все значения и ключи уникальны.

data = input().split(';')
dct = {}

for cell in data:
    k, v = cell.split('=')
    dct[k] = v

for k in sorted(dct):
    print('{} = {}'.format(k, dct[k]))

inverted_dct = {v: k for k, v in dct.items()}

print('#'*40)

for k in sorted(inverted_dct):
    print('{} = {}'.format(k, inverted_dct[k]))


# Результат:
# $ python3 task4.py
# php=Rasmus Lerdorf;perl=Larry Wall;python=Guido van Rossum
# perl = Larry Wall
# php = Rasmus Lerdorf
# python = Guido van Rossum
# ########################################
# Guido van Rossum = python
# Larry Wall = perl
# Rasmus Lerdorf = php

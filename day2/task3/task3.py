# task3:
# Напишите программу, которая принимает строку цветов, разделённых пробелами.
# Выведите первый и последний цвета и общее количество уникальных цветов.

colors = input().split()
print(colors[0], colors[-1], len(set(colors)))

# $ python3 task3.py
# red green red green black
# red black 3

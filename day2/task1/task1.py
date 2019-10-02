# task1:
# Напишите программу, которая проходит по списку и выводит,
# является ли значение типом int, float или не является численными типом.

lst = [1, 5445, 5445.0, 1.56, "1.90", "сорок_два", False, "", True]

for value in lst:
    if isinstance(value, (int, float)):
        print('Значение является типом int, float (или их подклассом)')
    else:
        print('Не является численным типом.')

# $ python3 task1.py
# Значение является типом int, float (или их подклассом)
# Значение является типом int, float (или их подклассом)
# Значение является типом int, float (или их подклассом)
# Значение является типом int, float (или их подклассом)
# Не является численным типом.
# Не является численным типом.
# Значение является типом int, float (или их подклассом)
# Не является численным типом.
# Значение является типом int, float (или их подклассом)

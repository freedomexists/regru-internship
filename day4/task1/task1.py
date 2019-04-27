# task1
# Написать программу которая в заданной строке
# s = 'this =- is , bad ! text #$%^123%^',
# заменяет все НЕ! буквы на пробелы.

import re
s = 'this =- is , bad ! text #$%^123%^'

pattern = '[^a-zA-Z]'
print(re.sub(pattern, ' ', s))

# Результат:
# $ python3 task1.py
# this    is   bad   text

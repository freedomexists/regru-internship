# Напишите скрипт, который будет открывать лог, и выводить кол-во ошибок модуля
# Kernel: System: Ticket: TicketPermission за 6 августа с 10:00 до 18:00.
# Сгруппируйте все ошибки, и выведите их от большего кол-ва упоминаний к меньшему.
# Запишите данные в файлы, названия которых будет датой ошибки
# (example: 02.01.2017.txt, 02.02.2017.txt, 02.05.2017.txt)

import datetime

errors_count = {}
with open('otrs_error.log', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.split(']')
        line = [elem.strip('[') for elem in line]
        try:
            date = datetime.datetime.strptime(line[0], '%a %b %d %H:%M:%S %Y')
        except ValueError:
            pass
        else:
            if datetime.datetime(2017, 8, 6, 10) <= date <= datetime.datetime(2017, 8, 6, 18):
                if line[2] in errors_count.keys():
                    errors_count[line[2]] += 1
                else:
                    errors_count[line[2]] = 1
    errors = sorted(errors_count, key=lambda i: errors_count[i], reverse=True)
    # print(['{} : {}'.format(i, errors_count[i])for i in errors_count])
    print([errors_count[i] for i in errors])

# task 3:
# Следует написать сервер и клиент с помощью socket

import socket
import json
import datetime
from operator import itemgetter
from sys import getsizeof


def search(content, date, module, i):
    l = 0
    r = len(content) - 1
    response = []

    while l <= r:
        mid = int((l + r) / 2)

        if i == 1:
            d = date.hour
            p = content[mid][0].hour
        elif i == 2:
            p = [content[mid][0].hour, content[mid][0].minute]
            d = [date.hour, date.minute]
        else:
            p = [content[mid][0].hour, content[mid][0].minute, content[mid][0].second]
            d = [date.hour, date.minute, date.second]
        if d == p:
            try:
                content[mid][1][33:content[mid][1].find(']', 33)].index(module)
            except ValueError:
                pass
            else:
                response.append(content[mid][1])
            content.pop(mid)
            l = 0
            r = len(content) - 1
        elif date > content[mid][0]:
            l = mid + 1
        elif date < content[mid][0]:
            r = mid - 1
    return response


def proc_request(data):
    date, module = data.split('-')
    date = [int(i) for i in date.split(':')]
    i = len(date)
    date = datetime.time(*date)
    return date, module, i


def read_log(pth):
    content = []
    with open('{}'.format(pth), 'r') as f:
        for line in f.readlines():
            try:
                time_arr = [int(i) for i in line[12:19].split(':')]
            except ValueError:
                pass
            else:
                content.append([datetime.time(time_arr[0], time_arr[1], time_arr[2]), line])
    return sorted(content, key=itemgetter(0))


sock = socket.socket()
sock.bind(('127.0.0.1', 8887))
sock.listen(5)
conn, addr = sock.accept()
print('Клиент подключился. IP ', addr)

content = read_log('otrs_error.log')

while True:
    data = conn.recv(1024)
    if not data:
        break
    date, module, i = proc_request(json.loads(data))
    response = json.dumps(search(content, date, module, i)).encode('utf-8')
    conn.send('{}'.format(getsizeof(response)).encode('utf-8'))
    conn.send(response)

conn.close()

# Результат
# $ python3 task3_server.py &
# [1] 1357
# $ python3 task3_client.py
# Введите строку в формате "HH[:MM[:SS]]-<some_string>" для поиска: 23:54-DB::CheckSessionID
# Клиент подключился. IP  ('127.0.0.1', 48688)
# Найдено 6 совпадений
# [Sun Apr  2 23:54:54 2017][Error][Kernel::System::AuthSession::DB::CheckSessionID][49] Got no SessionID!!
# [Sun Apr  2 23:54:49 2017][Error][Kernel::System::AuthSession::DB::CheckSessionID][49] Got no SessionID!!
# [Sun Apr  2 23:54:46 2017][Error][Kernel::System::AuthSession::DB::CheckSessionID][49] Got no SessionID!!
# [Sun Apr  2 23:54:24 2017][Error][Kernel::System::AuthSession::DB::CheckSessionID][49] Got no SessionID!!
# [Sun Apr  2 23:54:18 2017][Error][Kernel::System::AuthSession::DB::CheckSessionID][49] Got no SessionID!!
# [Sun Apr  2 23:54:15 2017][Error][Kernel::System::AuthSession::DB::CheckSessionID][49] Got no SessionID!!
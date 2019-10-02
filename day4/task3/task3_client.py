import socket
import json

s = input('Введите строку в формате "HH[:MM[:SS]]-<some_string>" для поиска: ')
try:
    _, _ = s.split('-')
except ValueError:
    print('Ошибка ввода')
sock = socket.socket()
sock.connect(('127.0.0.1', 8887))

json_req = json.dumps(s)
sock.send(json_req.encode('utf-8'))
size = sock.recv(128).decode('utf-8')
response = json.loads(sock.recv(int(size)+8).decode('utf-8'))

print('Найдено {} совпадений\n'.format(len(response)), ''.join([line for line in response]), sep='')


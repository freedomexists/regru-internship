# task 3:
# Следует написать сервер и клиент с помощью socket

import socket
import json
import datetime

def search(content, data, module):
    if data > content[content]

def proc_request(data):
    date, module = data.split('-')



def read_log(pth):
    content = []
    with open('{}'.format(pth), 'r') as f:
        for line in f.readlines():
            try:
                content.append([line[:26], line[26:33], line[33:]])
            except IndexError:
                pass
    return content


sock = socket.socket()
sock.bind(('127.0.0.1', 8887))
sock.listen(5)
conn, addr = sock.accept()
print('Клиент подключился. IP ', addr)

print(read_log('otrs_error.log')[0])

while True:
    data = conn.recv(1024)
    if not data:
        break
    response = proc_request(json.loads(data).decode())
    conn.send(response)

conn.close()
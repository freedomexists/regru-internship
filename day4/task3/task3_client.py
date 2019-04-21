import socket
import json

s = input('Введите строку в формате "HH[:MM[:SS]]-<some_string>" для поиска: ')
sock = socket.socket()
sock.connect(('127.0.0.1', 8887))

json_req = json.dumps(s.encode())
sock.send(json_req)
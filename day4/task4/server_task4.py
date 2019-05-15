import os
import socket


def main(sock):
    while True:
        conn, addr = sock.accept()
        pth = conn.recv(1024).decode('utf-8')
        print(pth)
        if os.path.isfile(pth):
            f = open('{}'.format(pth), 'rb')
            conn.send('Загружаю файл'.encode('utf-8'))
            l = f.read(1024)
            while l:
                conn.send(l)
                l = f.read(1024)
            conn.shutdown(socket.SHUT_WR)
            f.close()
        else:
            conn.send('Нет такого файла'.encode('utf-8'))


sock = socket.socket()
sock.bind(('127.0.0.1', 8887))
sock.listen(1)
main(sock)

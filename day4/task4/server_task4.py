import os
import socket


sock = socket.socket()
sock.bind(('127.0.0.1', 8887))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    print('Client connected', addr)
    request = conn.recv(1024).decode('utf-8')
    try:
        _, pth = request.split()
    except ValueError:
        conn.send('Format Error'.encode('utf-8'))
    else:
        print(request)
        if os.path.isfile(pth):
            f = open('{}'.format(pth), 'rb')
            conn.send('Загружаю файл'.encode('utf-8'))
            l = f.read(1024)
            while l:
                conn.send(l)
                l = f.read(1024)
                print(l)

            print('Файл отправлен')
            conn.shutdown(socket.SHUT_WR)
            f.close()
        else:
            conn.send('Нет такого файла'.encode('utf-8'))

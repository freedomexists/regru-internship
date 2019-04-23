import sqlite3
import socket

conn = sqlite3.connect('some.db')
c = conn.cursor()

sock = socket.socket()
ip, port = input('Введите ip:port сервера: ').split(':')
try:
    sock.connect((ip, int(port)))
except ConnectionError:
    print('Ошибка адреса')
else:
    while True:
        request = input('Введите запрос: ').split()
        if request[0] == 'get':
            filename = request[1].split('/')[-1]
            sock.send(' '.join(request).encode('utf-8'))
            l = sock.recv(1024)
            print(l.decode('utf-8'))
            if l.decode('utf-8') == 'Нет такого файла':
                break
            else:
                file = b''
                while l:
                    l = sock.recv(1024)
                    file += l
                print('Файл загружен')
                c.execute('INSERT INTO files (filename, file) VALUES (?, ?)', (filename, sqlite3.Binary(file)))
                conn.commit()
                break

        elif request[0] == 'cp':
            _, dpth, lpth = request
            filename = dpth.split('/')[-1]
            try:
                c.execute('SELECT * FROM files WHERE filename = ?', (filename, ))
                r = c.fetchone()
            except sqlite3.DatabaseError as err:
                print('Ошибка', err)
            else:
                if r:
                    with open('{}'.format(lpth), 'wb') as cp_file:
                        cp_file.write(r[1])
                    break
                else:
                    get_request = 'get {}'.format(dpth)
                    sock.send(get_request.encode('utf-8'))
                    l = sock.recv(1024)
                    print(l)
                    with open('{}'.format(lpth), 'wb') as cp_file:
                        while l:
                            l = sock.recv(1024)
                            cp_file.write(l)
                    break
    c.close()


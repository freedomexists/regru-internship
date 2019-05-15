import sqlite3
import socket

conn = sqlite3.connect('some.db')
c = conn.cursor()


def main(sock):
    while True:
        request = input('Введите запрос: ').split()
        method = request[0]
        if method == 'get':
            pth = request[1]
            get_file(sock, pth)

        elif method == 'cp':
            _, dpth, lpth = request
            filename = dpth.split('/')[-1]

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

def get_file(sock, pth):
    filename = pth.split('/')[-1]
    sock.send(pth.encode('utf-8'))
    response = sock.recv(1024).decode('utf-8')
    print(response)
    if response == 'Нет такого файла':
        return
    else:
        file = b''
        while response:
            response = sock.recv(1024)
            file += response
        print('Файл загружен')
        c.execute('INSERT INTO files (filename, file) VALUES (?, ?)', (filename, sqlite3.Binary(file)))
        conn.commit()
        break


def check_db(filename):
    try:
        c.execute('SELECT * FROM files WHERE filename = ?', (filename,))
        file = c.fetchone()
    except sqlite3.DatabaseError as err:
        print('Ошибка', err)
    else:
        return file


sock = socket.socket()
ip, port = input('Введите ip:port сервера: ').split(':')
try:
    sock.connect((ip, int(port)))
except ConnectionError:
    print('Ошибка адреса')

main(sock)
c.close()


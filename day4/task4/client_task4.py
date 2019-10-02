import sqlite3
import socket


def main(sock):
    conn = sqlite3.connect('some.db')
    c = conn.cursor()
    while True:
        request = input('Введите запрос: ').split()
        method = request[0]
        if method == 'get':
            pth = request[1]
            filename = pth.split('/')[-1]
            file = get_file(sock, pth)
            if file:
                c.execute('INSERT INTO files (filename, file) VALUES (?, ?)', (filename, sqlite3.Binary(file)))
                conn.commit()
                break
            else:
                break
        elif method == 'cp':
            _, dpth, lpth = request
            filename = dpth.split('/')[-1]
            data = check_db(filename, c)
            if data:
                with open('{}'.format(lpth), 'wb') as cp_file:
                    cp_file.write(data[1])
                break
            else:
                sock.send(dpth.encode('utf-8'))
                response = sock.recv(1024)
                print(response)
                with open('{}'.format(lpth), 'wb') as cp_file:
                    while response:
                        response = sock.recv(1024)
                        cp_file.write(response)
                break
    c.close()


def get_file(sock, pth):
    sock.send(pth.encode('utf-8'))
    response = sock.recv(1024).decode('utf-8')
    print(response)
    if response == 'Нет такого файла':
        return None
    else:
        file = b''
        while response:
            response = sock.recv(1024)
            file += response
        print('Файл загружен')
        return file


def check_db(filename, c):
    try:
        c.execute('SELECT * FROM files WHERE filename = ?', (filename, ))
        file = c.fetchone()
    except sqlite3.DatabaseError as err:
        print('Ошибка', err)
        return None
    else:
        return file


def create_socket_connection():
    sock = socket.socket()
    while True:
        ip, port = input('Введите ip:port сервера: ').split(':')
        try:
            sock.connect((ip, int(port)))
        except ConnectionError:
            print('Ошибка адреса')
        else:
            return sock


if __name__ == '__main__':
    sock = create_socket_connection()
    main(sock)



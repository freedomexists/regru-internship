import argparse
import socket


def create_connection(ip, port):
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM,
                         proto=0)
    try:
        sock.bind((ip, port))
        sock.listen(5)
        while True:
            client_sock, client_addr = sock.accept()
            return client_sock
    finally:
        sock.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Введите ip и port')
    parser.add_argument('--host',
                        dest='ip',
                        help='Необходимо указать ip-адрес сервера',
                        default='10.0.2.15')
    parser.add_argument('--port',
                        dest='port',
                        type=int,
                        help='Необходимо указать port-адрес сервера',
                        default='8887')
    args = parser.parse_args()
    while True:
        create_connection(args.ip, args.port)

    print(args.ip, type(args.port))

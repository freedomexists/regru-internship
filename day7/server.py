import argparse
import socket
from http_processes import process_request, process_response
from backend import run


def parse_cmd():
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

    return parser.parse_args()


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


def server(args):

    while True:
        conn = create_connection(args.ip, args.port)
        print('conn')
        req = conn.recv(4096)
        print(req)
        method, url, cookies = process_request(req)
        data = run(method, url, cookies)
        resp = process_response(data)
        conn.send(resp)
        if conn:
            conn.close()


if __name__ == '__main__':

    args = parse_cmd()
    server(args)



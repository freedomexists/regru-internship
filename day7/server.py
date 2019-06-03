import argparse
import socket
import datetime
from http_processes import process_request, process_response, HTTPError
from backend import run, get_show_errors_status, get_short_log_status


def logging_req(func):
    def wrap_log(*args, **kwargs):
        with open('log.txt', 'w') as log:
            result = func(*args, **kwargs)
            if get_short_log_status:
                log.write(result)
            else:
                log.write(*args, **kwargs)
        return wrap_log


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


def bind_sock(ip, port):
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM,
                         proto=0)

    sock.bind((ip, port))
    sock.listen(5)
    return sock


def create_connection(sock):
        while True:
            client_sock, client_addr = sock.accept()
            return client_sock


def recv_req(conn):
    tmpfile = conn.makefile('rb')
    return tmpfile

@logging_req
def unpack_req_data(req_file):   #костыль для реализации логирования
    method, url, cookies = process_request(req_file)
    return method, url, cookies


def server(args):

    sock = bind_sock(args.ip, args.port)

    while True:
        conn = create_connection(sock)
        req_file = recv_req(conn)

        try:
            method, url, cookies = unpack_req_data(req_file)
        except HTTPError as e:
            resp = process_response(e)
            conn.send(resp.encode('utf-8'))
            continue
        except ConnectionResetError as e:
            conn.send(e.strerror.encode('utf-8'))
            conn.close()
            break

        data = run(method, url, cookies)
        resp = process_response(data)
        conn.send(resp.encode('utf-8'))
        if conn:
            conn.close()


if __name__ == '__main__':

    args = parse_cmd()
    server(args)





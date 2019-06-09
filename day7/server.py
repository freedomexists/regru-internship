import argparse
import socket
import logging
import time
from http_processes import process_request, process_response, HTTPError
from backend import run, get_show_errors_status, get_short_log_status


def logging_req(func):
    def wrap_log(*args, **kwargs):
        logger = logging.getLogger('access_log')
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('access_log.log')
        log_format = logging.Formatter('[{asctime}]{message}', style='{')
        log_format.converter = time.gmtime
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
        result = func(*args, **kwargs)
        short_log = get_short_log_status()
        if short_log == 1:
            logger.info('[Method - {} :: URL - {} :: Cookie - {}]'.format(*result))
        if short_log == 0:
            logger.info('[Method - {} :: URL - {} :: Cookie - {} :: Headers - {} :: Body - {}]'.format(*result))
        return result
    return wrap_log


def parse_cmd():
    parser = argparse.ArgumentParser(description='Введите ip и port')
    parser.add_argument('--host',
                        dest='ip',
                        help='Необходимо указать ip-адрес сервера',
                        default='10.0.2.15') #10.0.2.15
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
            print(client_addr)
            return client_sock


def recv_req(conn):
    tmpfile = conn.makefile('rb')
    return tmpfile


@logging_req
def unpack_req_data(req_file):   #костыль для реализации логирования
    essential, headers, body = process_request(req_file)
    method, url, cookies = essential
    return method, url, cookies, headers, body


def server(args):

    sock = bind_sock(args.ip, args.port)

    while True:
        conn = create_connection(sock)
        req_file = recv_req(conn)

        try:
            method, url, cookies, headers, body = unpack_req_data(req_file)
            data, bg_color = run(method, url, cookies)
        except HTTPError as e:
            resp = process_response(e)
            conn.send(resp)
            continue
        except ConnectionResetError:
            print('Пришло не HTTP, сворачиваюсь.')
            conn.close()
            sock.close()
            break
        except TypeError:
            continue

        resp = process_response(data, bg_color=bg_color)
        conn.send(resp)
        if conn:
            conn.close()


if __name__ == '__main__':

    args = parse_cmd()
    server(args)





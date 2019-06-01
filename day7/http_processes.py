max_line_size = 64*1024


class HTTPError(Exception):
    def __init__(self, text, status):
        self.text = text
        self.status = status


def get_first_line(file):
    raw = file.readline(max_line_size + 1)

    if len(raw) > max_line_size:
        raise HTTPError('Request error. Превышена длинна первой строки запроса', 500)

    first_line_list = str(raw, 'iso-8859-1').rstrip('\r\n').split()

    if len(first_line_list) != 3:
        raise HTTPError('Invalid Request', 500)

    return first_line_list


def parse_headers(file):
    headers = []
    while True:
        line = file.readline(max_line_size + 1)

        if len(line) > max_line_size:
            raise HTTPError('Request error. Превышена длинна заголовка', 500)

        if line in {b'\r\n', b''}:
            break

        headers.append(line)

    dict_headers = {}
    for header in headers:
        k, v = header.decode('iso-8859-1').split(':')
        dict_headers[k] = v
    return dict_headers


def process_request(file):
    try:
        method, url, _ = get_first_line(file)
    except HTTPError as e:
        return e

    headers = parse_headers(file)
    cookie = headers.get('Cookie')
    return method, url, cookie


def error_resp(data):
    text = bytes(data.text)
    resp = {
        'status': data.status,
        'content-type': 'text',
        'reason': bytes(text),
        'Content-Length': len(text),
        'body': text,
        'data':
    }
    return resp


def process_response(data):

    if isinstance(data, Exception):  #TODO не забыть о show_error
        resp = error_resp(data)
    elif :
        resp = norm_resp

    return resp
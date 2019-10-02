max_line_size = 64*1024


class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body


def validate_status_line(line):
    if len(line) != 3:
        raise ConnectionResetError('Попытка взаимодействия не по HTTP. Работа сервиса прекращена.')
    if line[0] not in {'GET', 'POST'}:
        raise HTTPError(501, 'Not Implemented', 'Разрешены только GET и POST запросы')
    if line[2].strip('\r\n') != 'HTTP/1.1':
        raise HTTPError(505, 'HTTP Version Not Supported', 'Поддурживается только HTTP/1.1')


def get_first_line(file):
    raw = file.readline(max_line_size + 1)
    if len(raw) > max_line_size:
        raise HTTPError(414, 'URL Too Long', 'Превышена длинна первой строки запроса')

    first_line_list = str(raw, 'iso-8859-1').rstrip('\r\n').split()

    if first_line_list:
        return first_line_list


def parse_headers(file):
    headers = []
    while True:
        line = file.readline(max_line_size + 1)

        if len(line) > max_line_size:
            raise HTTPError(431, 'Request Header Fields Too Large', 'Превышена длинна заголовка')

        if line in {b'\r\n', b''}:
            break

        headers.append(line)

    dict_headers = {}

    for header in headers:
        k, v = header.decode('iso-8859-1').split(':', 1)
        dict_headers[k] = v.strip('\r\n')

    return dict_headers


def parse_cookie(headers):
    cookies = headers.get('Cookie').strip()
    if cookies:
        cookies = cookies.split(';')
        dict_cookie = {}

        for cookie in cookies:
            try:
                k, v = cookie.split('=')
            except ValueError:
                raise HTTPError(500, 'Bad request.', 'Неправильные печеньки')

            dict_cookie[k] = v

        return dict_cookie
    return None


def parse_body(file, headers):
    size = headers.get('Content-Length')
    if not size:
        return None
    return file.read(int(size))


def process_request(file):
    first_line = get_first_line(file)
    validate_status_line(first_line)
    method, url, _ = first_line
    headers = parse_headers(file)
    body = parse_body(file, headers)
    cookie = parse_cookie(headers)
    req_data = (method, url, cookie)
    return req_data, headers, body


def error_resp(data):
    data = (data.status, data.reason, data.body)
    resp = norm_resp(data)
    return resp


def norm_resp(data, add_headers=None, bg_color='', head='<head></head>'):

    status, reason, body = data
    content_type = 'text/html; charset=utf-8'

    status_line = 'HTTP/1.1 {} {}'.format(status, reason)
    html_body = ''.encode('utf-8')

    if bg_color:
        bg_color = ' BGCOLOR={}'.format(bg_color)

    if body:
        html_body = '<html>{}<body{}><div>'.format(head, bg_color) + body + '</div></body></html>'
        html_body = html_body.encode('utf-8')

    headers = {'Content-Type': content_type,
               'Connection': 'close',
               'Content-Length': len(html_body)}

    if add_headers:
        headers.update(add_headers)

    headers_line = ''

    for key, value in headers.items():
        headers_line += '{}: {}\r\n'.format(key, value)

    resp = status_line.encode('iso-8859-1') + b'\r\n'\
           + headers_line.encode('iso-8859-1') + b'\r\n'\
           + html_body + b'\r\n' + b'\r\n'
    return resp


def process_response(data, bg_color=None):

    if isinstance(data, Exception):
        resp = error_resp(data)
    elif len(data) == 3:
        resp = norm_resp(data, bg_color=bg_color)
    elif len(data) == 4:
        resp = norm_resp(data[:3], add_headers=data[3], bg_color=bg_color)

    return resp

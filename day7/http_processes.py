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
    print(headers)
    dict_headers = {}
    for header in headers:
        k, v = header.decode('iso-8859-1').split(':', 1)
        dict_headers[k] = v.strip('\r\n')
    return dict_headers


def parse_cookie(headers):
    cookies = headers.get('Cookie')
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


def process_request(file):
    first_line = get_first_line(file)
    print(first_line, len(first_line))
    validate_status_line(first_line)
    method, url, _ = first_line
    headers = parse_headers(file)
    cookie = parse_cookie(headers)
    req_data = (method, url, cookie)
    print(req_data)
    return req_data


def error_resp(data):
    data = (data.status, data.reason, data.body)
    resp = norm_resp(data)
    return resp


def norm_resp(data, add_headers=None, cookie=None):

    status, reason, body = data
    content_type = 'text/html; charset=utf-8'

    status_line = 'HTTP/1.1 {} {}'.format(status, reason)
    headers = {'Content-Type': content_type,
               'Content-Length': len(body)}

    if add_headers:
        headers.update(add_headers)

    headers_line = ''

    for key, value in headers.items():
        headers_line += '{}: {}'.format(key, value)

    if cookie and cookie.get('bg_color') == 'green':
        bg_color = ' BGCOLOR="#12e079"'
    else:
        bg_color = ' BGCOLOR="#fcfcfc"'

    html_body = '<html><head></head><body{}><div>'.format(bg_color) + body + '</div></body></html>'
    print(status_line, headers_line, html_body)
    resp = status_line.encode('iso-8859-1') + b'\r\n'\
           + headers_line.encode('iso-8859-1') + b'\r\n'\
           + html_body.encode('utf-8') + b'\r\n' + b'\r\n'
    print(resp)
    return resp


def process_response(data, cookie=None):

    if isinstance(data, Exception):  #TODO не забыть о show_error
        resp = error_resp(data)
    elif len(data) == 3:
        resp = norm_resp(data)
    elif len(data) == 4:
        resp = norm_resp(data[:4], data[4], cookie=cookie)
    print(resp)

    return resp

from http_processes import HTTPError

urls = {
    '',
    'show_errors',
    'div',
    'set_cookie',
    'short_log',
}
show_errors_switch = 0
short_log_switch = 0


def get_show_errors_status():
    return show_errors_switch


def get_short_log_status():
    return short_log_switch


def handler(method, url):
    url = url.split('/')[1:]
    if url[0] in urls:

        if url[0] == '' and method == 'GET':
            file = open('start.html', 'r', encoding='UTF-8')
            body = '\n'.join(file.readlines())
            file.close()
            data = (200, 'OK', body)
            return data

        elif url[0] == 'show_errors' and method == 'POST':
            if url[1] in {'1', '0'}:
                show_errors(url[1])
                data = (200, 'OK', 'OK')
                return data
            else:
                raise HTTPError(404, 'Not found', 'Страница не найдена')

        elif url[0] == 'div' and method == 'GET':

            if url[2] == 'to':
                return divide(url[1], url[3])
            else:
                raise HTTPError(404, 'Not found', 'Страница не найдена')

        elif url[0] == 'set_cookie' and method == 'GET':
            set_cookie = {}

            try:
                k, v = url[1].split('=')
            except ValueError:
                raise HTTPError(404, 'Not found', 'Страница не найдена')
            else:
                set_cookie['Set-Cookie'] = url[1] + '; path=/'
                data = (200, 'OK', 'OK', set_cookie)
                return data

        elif url[0] == 'short_log' and method == 'POST':
            global short_log_switch
            if url[1] == '1':
                 short_log_switch = 1
                 data = (200, 'OK', 'OK')
                 return data
            # elif url[1] == '0':
                # short_log_switch = 0
            else:
                raise HTTPError(404, 'Not found', 'Страница не найдена')

        else:
            raise HTTPError(405, 'Method Not Allowed', 'Адрес существует, но ожидается другой метод')

    raise HTTPError(404, 'Not found', 'Страница не найдена')


def cookie_handler(cookie):
    if cookie:
        color = cookie.get('bg_color')
        if color == 'green':
            bg_color = '#12e079'
        else:
            bg_color = '#fcfcfc'
        return bg_color


def run(method, url, cookie=None):
    bg_color = cookie_handler(cookie)

    try:
        data = handler(method, url)
    except ImportError:
        raise HTTPError(404, 'Not found', 'Страница не найдена')

    return data, bg_color


def show_errors(switch):
    global show_errors_switch
    if switch in {'1', '0'}:
        show_errors_switch = int(switch)
    else:
        raise HTTPError(404, 'Not found', 'Страница не найдена')


def divide(num1, num2):
    try:
        body = str(int(num1) / int(num2))
    except ValueError:
        status = 202
        reason = 'Accepted'
        body = 'Ошибка, переданные значения не ялвляются числами'
    except ZeroDivisionError:
        status = 202
        reason = 'Accepted'
        body = 'Ошибка, деление на ноль'
    else:
        status = 200
        reason = 'OK'
    finally:
        data = (status, reason, body)
        return data

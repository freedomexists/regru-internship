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
    return show_errors_switch


def handler(method, url):
    url = url.split('/')[1:]
    if url[0] in urls:
        if url[0] == '' and method == 'GET':
            start = open('start.html', 'r', encoding='UTF-8')
            body = '\n'.join(start.readlines())
            data = (200, 'OK', body)
            return data

        elif url[0] == 'show_errors' and method == 'POST':

            show_errors(url[1])
            data = (200, 'OK', None)
            return data

        elif url[0] == 'div' and method == 'GET':

            if url[3] == 'to':
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
                set_cookie['Set-Cookie'] = url[1]
                data = (200, 'OK', None, set_cookie)
                return data
        elif url[0] == 'short_log' and method == 'POST':
            global short_log_switch
            if url[1] == '1':
                short_log_switch = 1
            # elif url[1] == '0':
                # short_log_switch = 0
        else:
            raise HTTPError(405, 'Method Not Allowed', 'Адрес существует, но ожидается другой метод')

    raise HTTPError(404, 'Not found', 'Страница не найдена')


def cookie_handler(cookie):
    if cookie.get('bg-color') == 'green':
        return True


def run(method, url, cookie=None):
    data = handler(method, url)


    return data


def show_errors(switch):
    global show_errors_switch
    if switch in {'1', '0'}:
        show_errors_switch = int(switch)
    else:
        raise HTTPError()


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

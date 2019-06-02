from http_processes import HTTPError

urls = {
    '/',
    '/show_errors',
    '/div',
    '/set_cookie',
    '/short_log',

}
show_errors_switch = 0


def handler(method, url):
    if url in urls:
        if url[0] == '/' and method == 'GET':
            body =
            return tuple(200, 'OK', body)
        if url[0] == '/show_errors' and method == 'POST':
            show_errors(url[1])
            return
    raise HTTPError(404, 'Not found', 'Страница не найдена')


def run(method, url, cookies):
    data = handler(method, url)
    return data


def show_errors(switch):
    global show_errors_switch
    show_errors_switch = switch

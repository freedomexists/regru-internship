# task2
# Написать регулярное выражение которое выделяет ВЕРНЫЕ ссылки на картинки в разных HTML документах.
import re
import requests

img_formats = ['jpg', 'jpeg', 'bmp', 'gif', 'tif', 'png']
with open('some.html', 'r', encoding='utf-8') as f:
    data = f.read()
    pattern = r'https?://[^\"\s>]+'
    maybevalids = re.findall(pattern, data)
    for ref in maybevalids:
        try:
            response = requests.get(ref)
        except requests.exceptions.SSLError:
            pass
        if 'Content-Disposition' in response.headers:
            if response.headers['Content-Disposition'].split('.')[-1] in img_formats:
                print(ref)

# Результат
# $ python3 task2.py
# https://img-fotki.yandex.ru/get/9931/160700675.0/0_110e34_54188f48_-1-orig
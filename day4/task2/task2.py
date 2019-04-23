import re
import requests


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
            if response.headers['Content-Disposition'].split('.')[-1] in ['jpg', 'jpeg', 'bmp', 'gif', 'tif', 'png']:
                print(ref)

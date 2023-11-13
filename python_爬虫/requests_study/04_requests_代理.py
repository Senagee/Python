import json

import requests

url = 'http://www.baidu.com/s?'

data = {
    'wd': 'ip'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

proxy = {
    'http': '182.34.26.32:9999'
}

response = requests.get(url = url, params = data, headers = headers)

response.encoding = 'utf8'
with open('daili.html', 'w', encoding = 'utf8') as fp:
    fp.write(response.text)
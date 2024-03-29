"""
使用代理访问浏览器，handler是基础
handler build_opener    open
"""

import urllib.request

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url, headers = headers)

# （1） 获取handler对象
handler = urllib.request.HTTPHandler()

# （2） 获取opener对象
opener = urllib.request.build_opener()

response = opener.open(request)

print(response.read().decode('utf-8'))



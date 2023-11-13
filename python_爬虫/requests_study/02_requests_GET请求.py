"""
    (1)
    (2) 不需要定制请求对象

"""


import requests

url = 'https://www.baidu.com/s'

data = {
    'wd': "美女"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# url = url地址  params = 请求的参数  **kwargs:参数字典
response = requests.get(url = url, params = data, headers = headers)

response.encoding = 'utf8'

print(response.url)






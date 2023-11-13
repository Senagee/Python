"""
实际上是urllib的封装类


urllib:
    (1) 一个类型六个方法
    (2) get请求
    (3) post请求
    (4) ajax的get请求
    (5) ajax的post请求
    (6) Cookie免登录 微博
    (7) 代理

request:
    (1) 一个类型和六个属性
    (2) get请求
    (3) post请求
    (4) 代理
    (5) Cookie免登录, 验证码
"""

# 一个类型6个属性

import requests

url = 'https://www.baidu.com/'

response = requests.get(url)
# requests.models.Response类型
print(type(response))

response.encoding = 'utf8'
# 获取网页源码
print(response.text)

# 获取网页源码,放回一个Bytes类型
print(response.content)

# url地址
print(response.url)

# 响应的状态码
print(response.status_code)

# 响应头
print(response.headers)
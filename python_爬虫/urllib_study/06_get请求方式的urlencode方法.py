"""
urllib.parse.urlencode(param: 字典)方法的适用场景： 在get请求中将多个 中文 参数转换成 unicode编码
    参数是一个字典
"""

import urllib.request
import urllib.parse

# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD

new_url = "https://www.baidu.com/s?"

data = {
    'wd': "周杰伦",
    "sex": "男",
    "location": "中国"
}
new_data = urllib.parse.urlencode(data)

url = new_url + new_data

# print(url)

# 定制request对象
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36 Edg/119.0.0.0"
}

request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器发送请求

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

print(type(content))
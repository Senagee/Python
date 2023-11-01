import urllib.request

import urllib.request

# 输入一个访问的url地址
my_http = "http://baidu.com"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(my_http)

# 获取数据
    # response.read()的返回值是bytes需要进行解码操作
data = response.read().decode("utf-8")

print(type(data))


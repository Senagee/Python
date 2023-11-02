import urllib.request

import urllib.request

# 输入一个访问的url地址
my_http = "http://www.baidu.com"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(my_http)

# 读取网页的源码
    # response.read()的返回值是bytes需要进行解码操作
content = response.read(5).decode("utf-8")

print(content)


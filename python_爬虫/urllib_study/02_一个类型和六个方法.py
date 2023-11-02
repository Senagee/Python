#

"""
一个类型：
    HTTPResponse
六个方法：
    read()
    readline()
    readlines()
    getcode()
    geturl()
    getheaders()

"""
import urllib.request

my_url = "http://www.baidu.com"

response = urllib.request.urlopen(my_url)

# 一个类型
# HTTPResponse
# print(type(response))

# content = response.read()
# print(content)

    # 扩展
# content = response.read(5)    # 5个字节
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# return list
# content = response.readlines()
# print(type(content))

# getcode()
# content = response.getcode() # 返回状态码
# print(content)

# geturl()
# content = response.geturl() # 返回url地址
# print(content)

# getheaders()
# content = response.getheaders()  # 获取状态信息
# print(content)



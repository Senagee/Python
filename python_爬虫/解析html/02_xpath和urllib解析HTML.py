#
import urllib.request

from lxml import etree

url = 'https://www.baidu.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36 Edg/119.0.0.0"
}

# 定制请求对象
request = urllib.request.Request(url = url, headers = headers)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
# print(content)

tree = etree.HTML(content)

result = tree.xpath('//input[@id="su"]/@value')
print(result)
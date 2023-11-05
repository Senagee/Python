"""
quote方法， 将中文转换成unicode编码

"""




# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6


import urllib.parse
import urllib.request


url = 'https://www.baidu.com/s?wd='
# print(url)

# 要将中文转换成unicode编码
name_unicode = urllib.parse.quote("周杰伦")

url = url + name_unicode
# print(url)

# 反爬UA
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))





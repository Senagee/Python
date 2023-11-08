# 使用代理ip访问浏览器数据


"""
报错：ip问题
"""
import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url, headers = headers)

proxies = {
    'http': '114.231.42.53:8888'
}

# 创建代理对象
handler = urllib.request.ProxyHandler(proxies = proxies)

# 创建opener对象
opener = urllib.request.build_opener(handler)

# 模拟浏览器向客户端发送请求
response = opener.open(request)

content = response.read().decode('utf8')

# 下载
with open('IP.html', 'w', encoding='utf8') as f:
    f.write()
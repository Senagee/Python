#
# https://haokan.baidu.com/v?pd=wisenatural&vid=9842186318154565762
"""# url的组成：
            协议           主机                 端口号          路劲          参数             锚点
        http/https      haokan.baidu.com                      v          pd= &id=          #
https比http相对安全

"""

# UA（User Agent）：包括用户的操作系统一系列信息，，反爬手段

import urllib.request

my_url = "https://www.baidu.com/"
# 遇到反爬UA
    # 由于我们是程序发起的请求，服务器识别出不是浏览器的请求
    # 这里我们需要进行伪装
# 定制请求对象
    # 获取对应浏览器的UA数据
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

# 因为参数顺序，这里要用关键字传参
request = urllib.request.Request(url=my_url, headers=headers)
response = urllib.request.urlopen(request)

print(response.read())



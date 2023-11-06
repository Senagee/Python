import urllib.request
import urllib.parse

# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname

url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

data = {
    'cname': '佛山',
    'pid': '',
    'pageIndex': '1',
    'pageSize': '10'
}

data = urllib.parse.urlencode(data).encode()
#
request = urllib.request.Request(url=url, headers=headers, data=data)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)
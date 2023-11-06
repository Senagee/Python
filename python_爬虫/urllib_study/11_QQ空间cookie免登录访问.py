# https://user.qzone.qq.com/2628255714

import urllib.request

url = 'https://user.qzone.qq.com/2628255714'

headers = {
    # ':authority': 'user.qzone.qq.com',
    # ':method': 'GET',
    # ':path': '/2628255714',
    # ':scheme': 'https',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'If-Modified-Since:Mon, 06 Nov 2023 13:27': '59 GMT',
    # # cookie是核心
    # 'Cookie':'eas_sid=Q1U6d9T4T6E9Z8F7M8b5J819b7; pgv_pvid=596574712; RK=KUvFij1ov9; ptcz=4789a223a8f7b5f5660a2046308f8ad8981539220934fb2f50fdd4caf66d3210; uin=o2628255714; _qpsvr_localtk=0.5532822086531675; pgv_info=ssid=s4352928527; skey=@gtyI5nqpY; p_uin=o2628255714; pt4_token=KmXe*Tfq7N-NKlw8qgFz9lDmmyw6gsKsN2K0*pncnOk_; p_skey=5qZJjBT74WBXEua1Hs7PeegpKhzNKrAJO-FoPBDBI-c_; Loading=Yes; x-stgw-ssl-info=101247dbd8bb12c1dc3e9c2dab5c29a3|0.101|-|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|10054|h2|0; qz_screen=1280x720; 2628255714_todaycount=0; 2628255714_totalcount=6181; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0',
    # # 这个也是反爬，你的上一个网站是这个
    # 'Referer': 'https://qzs.qq.com/',
    # 'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    # 'Sec-Ch-Ua-Mobile': '?0',
    # 'Sec-Ch-Ua-Platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'same-site',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
# print(content)

with open('qq空间.html', 'w', encoding='utf8') as f:
    f.write(content)

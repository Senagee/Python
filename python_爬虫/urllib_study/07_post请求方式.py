"""
post请求方式的反爬：
    要将浏览器中的headers，data获取到模拟的请求对象中去，在headers中COOKIE对象是关键，UA都可以不要

"""

import urllib.request
import urllib.parse
import json

url = "https://fanyi.baidu.com/v2transapi?from=srp&to=zh"

# 定制POST方式的request对象

data = {
    'from':'en',
    'to':'zh',
    'query':'spider',
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'63766.268839',
    'token':'394c3fb2e91fe596baee3e7ff4d5236e',
    'domain':'common',
    'ts':'1699185548935'
}
# 定制POST的请求对象时，参数中的数data必须是byte类型的，所以在数据转换成unicode编码后还要在进行一次编码
data = urllib.parse.urlencode(data).encode("utf8")

headers = {
    # 'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate, br',      # 这行必须注释，不然会报错UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Acs-Token':'1699185370060_1699185548957_vs6TRP/fYK+IAWeWYxU7/qOswRe/PV9eW10y8AechbEVUC2jpkeJODHsxf3wd/jfWAecrX2OJa4fx5UTetBTZUwz9k3W1jn7gxX2klDq3CRcjMgr/W9I4oOaAqwnZ/HL1oAd4/tGIiu8JtxfNhRx1uyqz+jvslG0S2SRbiCLd+8OADNH+aqZkZmFNljsYkCdOgEm1l8fT0C/5CDX6qmKIfIzNGBgEu/t+LUmTNt9zqkNNENd1kF2UMChs/VTUth+nYYt0PrP0rc4JzMFnH4RzrRbiN6zTj6kKKrQ7m4nS234YCSDmYTildzaDrXcIMT+gvAvjA7JwcrFWU6B7UuaMQSMkReCS6dd9fzvSGKHa2eizZVBohpcDDn/VrA2Rwl1lwXMdpRWpdb+2N2X4wlHQJbZ9yNv53GSqQQlk2aow6qji+sifNOt2Mz411VVSPQShRTxKVFofyZjgAZHaDjKTubMLTLMpTQRg1D1ip+nMBjggRsLjwVORnBXmuvjApGk',
    # 'Connection':'keep-alive',
    # 'Content-Length':'153',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'BDUSS=np4b1U4dHo1R1FrSGlodHlEc2ZMaFUwbn5IdzU1aHdEWXNDWUM5YzRGYnJxMWhsRVFBQUFBJCQAAAAAAAAAAAEAAAC6G6P5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOseMWXrHjFlS; BDUSS_BFESS=np4b1U4dHo1R1FrSGlodHlEc2ZMaFUwbn5IdzU1aHdEWXNDWUM5YzRGYnJxMWhsRVFBQUFBJCQAAAAAAAAAAAEAAAC6G6P5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOseMWXrHjFlS; BIDUPSID=9EC30898D68A1D42FD2B020ED1C30BCB; PSTM=1698893078; BAIDUID=9BECD66F3D275B4262DECE0432F9B891:FG=1; BAIDUID_BFESS=9BECD66F3D275B4262DECE0432F9B891:FG=1; RT="z=1&dm=baidu.com&si=efdb9ab0-ca76-4c72-b715-411ed0062904&ss=logn2nz8&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3j8&ul=1bhac&hd=1bhb4"; ZFY=YCfH:ArbAhvgMDGjQ:BwnG7lIlLtHHuqpOggAFRLTbYxs:C; BA_HECTOR=ak040g2120208h0ha4a00la51ikf0ci1q; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=7; delPer=0; H_PS_PSSID=39396_39531_39419_39592_39437_39526_39497_26350_39560; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=11047525072563755679; BCLID_BFESS=11047525072563755679; BDSFRCVID=W60OJexroG3O1HvqOkiEboxrt_weG7bTDYrEOwXPsp3LGJLVFdWiEG0Pts1-dEu-S2OOogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=W60OJexroG3O1HvqOkiEboxrt_weG7bTDYrEOwXPsp3LGJLVFdWiEG0Pts1-dEu-S2OOogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsL5KjB2Q-XPoO3KOchqnCKfnOMfLVhp7H-pRf5mkf3fbgy4op8P3y0bb2DUA1y4vp0t3U2mTxoUJ2-KDVeh5Gqq-KXU4ebPRiJ-b9Qg-JKpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjLKD5Q-3H; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsL5KjB2Q-XPoO3KOchqnCKfnOMfLVhp7H-pRf5mkf3fbgy4op8P3y0bb2DUA1y4vp0t3U2mTxoUJ2-KDVeh5Gqq-KXU4ebPRiJ-b9Qg-JKpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjLKD5Q-3H; APPGUIDE_10_6_6=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1699185058; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1699185069; ab_sr=1.0.1_NzQ1OWViNjIwYjZiZDI3ZmJhNjI4MWM4MjAzZTIyMTczYWJiOTU0MDlhYjY0ZTczZjhlODhlMGQ5NTQ5NmYzOTViNmUyZTU4NDkwMmY4MTg4OTkyZmY0NTFmYzg1ZGI3NWUxY2M1N2VhZTM5MjZhN2M4OWRjMDBjODY2ODIwNjk4MGY3MmFjNmNmMTVlZTlhYWYwNDgzMmZiMWRmMTY3OGQxNDM0MDJlMzViNzg4NmRkMzNkMTI2MzMwN2IxNjhj',
    # 'Host':'fanyi.baidu.com',
    # 'Origin':'https://fanyi.baidu.com',
    'Referer':'https://fanyi.baidu.com/translate?aldtype=16047&query=spide%0D%0A&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    # 'Sec-Ch-Ua':'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    # 'Sec-Ch-Ua-Mobile':'?0',
    # 'Sec-Ch-Ua-Platform':'"Windows"',
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-origin',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    # 'X-Requested-With':'XMLHttpRequest'
}

#

request = urllib.request.Request(url=url, data=data, headers=headers)
# print(type(request))


response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

content = json.loads(content)
print(content)



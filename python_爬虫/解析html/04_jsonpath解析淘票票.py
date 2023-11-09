# https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1699532194265_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true
import json
import urllib.request

import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1699532194265_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # :authority:dianying.taobao.com
    # :method:GET
    # :path:/cityAction.json?activityId&_ksTS=1699532194265_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true
    # :scheme:https
    'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Bx-V':'2.5.3',
    'Cookie':'t=bc7a92ac4e1b2ad982653ebf6b4c280c; cookie2=1f51101a33df485ad66bdb0f72f8fa5a; v=0; _tb_token_=e637333f38e4; xlly_s=1; tfstk=dVw23jmbPtBVV-0f9jDZUpbWbZkxCvQCQRgsjlqicq0cWSMa_oaq1rZi5Aza7PujsZHbQzkYFS9slZHajyMNRw6CdoExeAbCRcA0Ytn504NJk9ZYDAK2SMNlddSJFNs9o2tvgdlA-lguH3eSJhdK44JMLHnqiFE21dJNhmcm-b0cQbYtqINTBS8M_jm-42sP4bivvf5..; l=fBaREVbePRLJAXdwBO5CFurza77trIRb8sPzaNbMiIEGa6tP9eHkrNCT9siHWdtjgTfbQetyMAhYGdeHyd4d0giMW_N-1NKDjxJ6-bpU-L5..; isg=BIOD9Rg24qaMHq5SaVSfUKASEkct-Bc67FS0QLVgFuJ7dKKWPcwHilyi7gQ6VG8y',
    'Referer':'https://dianying.taobao.com/',
    'Sec-Ch-Ua':'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'mpty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
# print(content)

content = content.split("(")[1].split(")")[0]
# print(content)

with open("淘票票.json", "w", encoding='utf-8') as f:
    f.write(content)

#
obj = json.load(open("淘票票.json", "r", encoding="utf8"))
name_list = jsonpath.jsonpath(obj, "$..regionName")
print(name_list)
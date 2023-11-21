"""
    在登录页面中点击登录，进入登录接口，发现还需要很多参数
变换    __VIEWSTATE:
变换    __VIEWSTATEGENERATOR:
        from: http://so.gushiwen.cn/user/collect.aspx
        email: 18934299467
        pwd: 111111
变换     code: 验证码

    在登录网页中发现id为：__VIEWSTATE、__VIEWSTATEGENERATOR两个隐藏域
    说明需要在登录网页中获取它们两个的值
"""
import requests

# 在登录页面获取 __VIEWSTATE、__VIEWSTATEGENERATOR的值
    # 登录页面url
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

login_page_response = requests.get(url = url, headers = headers)

login_page_content = login_page_response.text
# print(content)

# 解析XML
    # 获取__VIEWSTATE、__VIEWSTATEGENERATOR
from lxml import etree

tree = etree.HTML(login_page_content)

viewstate = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
print(viewstate)

viewstategenerator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
print(viewstategenerator)

    # 验证码获取
code_src = tree.xpath('//img[@id="imgCode"]/@src')[0]
# print(code_src)

# 将验证码下载在本地，观察图片，进行登录
code_url = "https://so.gushiwen.cn" + code_src
# print(code_url)


# """
#       以下代码有坑`\（不能使用urlretrieve直接下载）
#       在访问登录网页时进行了第一次访问
#       在访问验证码时又进行了一次访问
#       所以下载的验证码是无效的！
#       要使用session技术
# """
# import urllib.request
# urllib.request.urlretrieve(url = code_url, filename="code.png")

session = requests.session()

code_response = session.get(code_url)

# 保存图片用二进制
code_content = code_response.content

with open('code.png', "wb") as fp:
    fp.write(code_content)

code = input("请输入验证码：")

# 登录接口
# 登录接口url
interface_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.asp"

data = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2628255714@qq.com',
    'pwd': 'sheng..+',
    'code': code,
    'denglu': '登录'
}
response = session.post(url = url, headers = headers, data = data)


with open("login.html", "w",encoding="utf8") as fp:
    fp.write(response.text)

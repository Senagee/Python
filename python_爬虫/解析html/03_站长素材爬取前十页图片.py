# 第一页url https://sc.chinaz.com/tupian/fengjing.html
# 第二页url https://sc.chinaz.com/tupian/fengjing_2.html
import urllib.request

from lxml import etree


# 定制请求对象
def create_request(page: int):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/fengjing.html'
    else:
        url = 'https://sc.chinaz.com/tupian/fengjing_' + str(page) + '.html'
    # print(url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                      "Safari/537.36 Edg/119.0.0.0",
        "Referer":
            "https://sc.chinaz.com/tupian/fengjing.html"
    }
    return urllib.request.Request(url=url, headers=headers)


# 获取网页内容
def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf8')


# 下载
def down_load(content):
    # print(content)
    tree = etree.HTML(content)

    # xpath解析获取图片src，所有网站图片都会进行一个懒加载（只有浏览到了才显示图片）,所以此处不能用src
    data_original_list = tree.xpath('//div[@class="container"]//img/@data-original')
    # print(len(src_list))
    # xpath解析获取图片名
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    # print(len(name_list))

    # 下载
    for i in range(len(name_list)):
        f_name = "./Img/" + name_list[i] + ".jpg"
        url = "https:" + data_original_list[i]

        # print(url)
        urllib.request.urlretrieve(url = url, filename=f_name)



if __name__ == '__main__':
    start_page = int(input('请输入起始页：'))
    end_page = int(input('请输入结束页：'))
    for page in range(start_page, end_page + 1):
        # print(page)
        # 定制请求对象
        request = create_request(page)
        # 获取网页内容
        content = get_content(request)
        # 下载
        down_load(content)

import urllib.parse
import urllib.request


# 定制请求对象（GET请求）
def create_request(page: int):
    begin_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    url = begin_url + data

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                      "Safari/537.36 Edg/119.0.0.0"
    }
    print(url)
    return urllib.request.Request(url=url, headers=headers)


# 获取响应数据
def get_content(request):
    response = urllib.request.urlopen(request)

    return response.read().decode('utf8')


# 下载到本地
def down_load(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf8') as f:
        f.write(content)

#        https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
#        https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20

# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
if __name__ == '__main__':
    begin_page = int(input('起始页：'))
    end_page = int(input('结束页：')) + 1
    for page in range(begin_page, end_page):
        # print(page)
        # 定制请求对象
        request = create_request(page)
        # 获取响应数据
        content = get_content(request)
        # 下载到本地
        down_load(page, content)
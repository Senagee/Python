# 下载 urlretrieve(url, "自定义文件名称")

import urllib.request

# 下载网页
# url_page = "http://www.wuwenwen.top/"
# urllib.request.urlretrieve(url_page, "吴小姐的网站.html")

# 下载图片
# url_img = "https://wuwenwen.top/2023/04/21/%E5%9B%BE%E7%89%87/1.jpg"
# urllib.request.urlretrieve(url_img, "吴小姐的照片.jpg")

# 下载视频
url_vidio =  "https://vd4.bdstatic.com/mda-mh9fe7kfeqhm19xt/sc/cae_h264/1628593490984747144/mda-mh9fe7kfeqhm19xt.mp4?v_from_s=hkapp-haokan-hnb&auth_key=1698907236-0-0-f0c4f3e3d0164e5713b29dba9716d265&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=2436555186&vid=9842186318154565762&klogid=2436555186&abtest=114240_1"
urllib.request.urlretrieve(url_vidio, "vidio.mp4")

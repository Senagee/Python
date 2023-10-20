#
import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("D:/python/python-learn/pyecharts_可视化图表/疫情.txt", "r", encoding="utf-8")
data_str = f.read()
f.close()
dict_data = json.loads(data_str)

# 从字典中取出数据
province_data_list = dict_data["areaTree"][0]["children"]

data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]                   # 省份名称
    province_confirm = province_data["total"]["confirm"]    # 确诊人数
    data_list.append((province_name, province_confirm))

print(data_list)

# 创建地图对象

my_map = Map()

my_map.add("各省份确诊人数", data_list, "china")

my_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"}
        ]

    )
)

my_map.render("全国疫情地图.html")
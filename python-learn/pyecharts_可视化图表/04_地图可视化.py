from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map1 = Map()

data = [
    ("广东", 19991),
    ("福建", 99),
    ("黑龙江", 1999),
    ("上海", 2199),
    ("北京", 59),
    ("广西", 10000),
    ("南海", 888)
]

print(data)
map1.add("测试地图", data_pair=data, maptype="china")

map1.set_global_opts(
    
    visualmap_opts=VisualMapOpts(
        is_show=False,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#CC6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"},
        ]
    )
)
map1.render()

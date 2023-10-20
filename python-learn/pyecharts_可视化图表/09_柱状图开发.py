#
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

f = open("D:/python/python-learn/pyecharts_可视化图表/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_list = f.readlines()
data_list.pop(0)

data_dict = {}

for list in data_list:
    year = int(list.split(",")[0])
    country = list.split(",")[1]
    gdp = float(list.split(",")[2])
    try:
        # 查看字典中是否已有这个年份
        data_dict[year].append([country, gdp])
    except KeyError as e:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 字典中的key是乱序的，先排序
years_list = sorted(data_dict.keys())

timeline = Timeline({
    "theme": ThemeType.LIGHT
})

for year in years_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 前八
    datas = data_dict[year][0:8]
    x_data = []
    y_data = []
    for data in datas:
        x_data.append(data[0])
        y_data.append(data[1]/100000000)
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}全球前八GPT数据")
    )
    timeline.add(bar, year)


timeline.add_schema(
    play_interval=100,
    is_loop_play=False
)


timeline.render("1960-2019全球前8GTP.html")

#
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

f_us = open("D:/python/python-learn/pyecharts_可视化图表/美国.txt", "r", encoding="utf-8")
f_jp = open("D:/python/python-learn/pyecharts_可视化图表/日本.txt", "r", encoding="utf-8")
f_in = open("D:/python/python-learn/pyecharts_可视化图表/印度.txt", "r", encoding="utf-8")

#
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend Key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']


# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))


# 全局设置
line.set_global_opts(
    title_opts=TitleOpts(title="美日印三国2020年新冠确诊人数", pos_left="center", pos_bottom="1%")
)

line.render()

f_in.close()
f_jp.close()
f_us.close()


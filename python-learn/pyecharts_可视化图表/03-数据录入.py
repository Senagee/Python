#
import json

f_us = open("D:/python/python-learn/pyecharts_可视化图表/美国.txt", "r", encoding="utf-8")

#
us_data = f_us.read()
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]

# JSON转Python字典
us_dict = json.dumps(us_data)

# 获取trend Key
trend_data = us_dict["data"][0]['trend']

# 获取日期数据，用于x轴，取2020年（到314下标结束）
x_data = trend_data['updateDate'][:314]

# 获取确认数据，用于y轴，取2020年（到314下标结束）
y_data = trend_data['list'][:314]

# 生成图表
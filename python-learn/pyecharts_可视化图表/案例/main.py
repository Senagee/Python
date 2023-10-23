#
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import TitleOpts, LabelOpts, InitOpts

from pyecharts_可视化图表.案例.file_define import TextFileReader, JSONFileReader
from pyecharts_可视化图表.案例.data_define import Record

text_file_data = TextFileReader("2011年1月销售数据.txt").reader()
json_file_data = JSONFileReader("2011年2月销售数据JSON.txt").reader()

file_data: list[Record] = text_file_data + json_file_data

# 计算一个月每一天的销售额的销售额 dict_date = {"2011-1-1": 100 , "2011-1-2": 200}
dict_date = {}
for record in file_data:
    # 这个日期是否在这个字典中
    if record.date in dict_date.keys():
        # 在的话说明这个日期已经存在，做累加
        dict_date[record.date] += record.money
    else:
        #
        dict_date[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(dict_date.keys()))
bar.add_yaxis("销售额", list(dict_date.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")
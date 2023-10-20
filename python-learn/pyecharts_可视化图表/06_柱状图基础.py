# 反转xy轴、

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

my_bar = Bar()

my_bar.add_xaxis(["美国", "英国", "日本"])
my_bar.add_yaxis("美英日三国GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转x、y轴
my_bar.reversal_axis()

my_bar.render("基础柱状图构件.html")


# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts

# 获取图表对象
line = Line()

# 定义X轴
line.add_xaxis(["中国", "美国", "英国"])

# 定义Y轴
line.add_yaxis("GTP", [30, 20, 10])

# 全局配置 set_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title="GTP图示", pos_left="center", pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 使用render()将代码生成图表
line.render()
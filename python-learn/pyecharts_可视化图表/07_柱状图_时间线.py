from pyecharts.charts import Timeline, Bar
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

bar1 = Bar()
bar2 = Bar()
bar3 = Bar()

bar1.add_xaxis(["美国", "英国", "日本"])
bar1.add_yaxis("美英日三国GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2.add_xaxis(["美国", "英国", "日本"])
bar2.add_yaxis("美英日三国GDP", [50, 30, 40], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3.add_xaxis(["美国", "英国", "日本"])
bar3.add_yaxis("美英日三国GDP", [60, 50, 45], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 时间线对象
timeline = Timeline(
    {
        "theme": ThemeType.LIGHT
    }
)

timeline.add(bar1, "1960")
timeline.add(bar2, "1961")
timeline.add(bar3, "1962")

# 自动播放设置
timeline.add_schema(
    play_interval=1000
)

timeline.render("柱状图时间线绘图.html")



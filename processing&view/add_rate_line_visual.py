import pyecharts.options as opts
from pyecharts.charts import Line
import day_add_process_data
import tools


x_data = tools.to_list(day_add_process_data.get_day().values)
y_data_1 = tools.to_list(day_add_process_data.get_dead_rate().values)
y_data_2 = tools.to_list(day_add_process_data.get_heal_rate().values)


def draw():
    (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="当日死亡率",
            y_axis=[float(i) for i in y_data_1],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="当日治愈率",
            y_axis=[float(i) for i in y_data_2],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="当日死亡/治愈率折线图"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
        .render("../view/两月内每日死亡治愈率.html")
    )

import pyecharts.options as opts
from pyecharts.charts import Line
import day_all_process_data
import tools


x_data = tools.to_list(day_all_process_data.get_day().values)
y_data_1 = tools.to_list(day_all_process_data.get_confirm().values)
y_data_2 = tools.to_list(day_all_process_data.get_local_confirm().values)
y_data_3 = tools.to_list(day_all_process_data.get_dead().values)
y_data_4 = tools.to_list(day_all_process_data.get_heal().values)


def draw():
    (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="现存确诊",
            y_axis=[int(i) for i in y_data_1],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="本土现存确诊",
            y_axis=[int(i) for i in y_data_2],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="总死亡",
            y_axis=[int(i) for i in y_data_3],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="总治愈",
            y_axis=[int(i) for i in y_data_4],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="折线图堆叠"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
        .render("../view/两月内每日总数.html")
    )

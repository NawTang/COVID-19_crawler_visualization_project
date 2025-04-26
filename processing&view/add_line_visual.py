import pyecharts.options as opts
from pyecharts.charts import Line
import day_add_process_data
import tools


x_data = tools.to_list(day_add_process_data.get_day().values)
y_data_1 = tools.to_list(day_add_process_data.get_local_confirm_add().values)
y_data_2 = tools.to_list(day_add_process_data.get_confirm_add().values)
y_data_3 = tools.to_list(day_add_process_data.get_wzz_add().values)
y_data_4 = tools.to_list(day_add_process_data.get_local_wzz_add().values)
y_data_5 = tools.to_list(day_add_process_data.get_dead_add().values)
y_data_6 = tools.to_list(day_add_process_data.get_heal_add().values)


def draw():
    (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="本土新增确诊",
            y_axis=[int(i) for i in y_data_1],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="新增确诊",
            y_axis=[int(i) for i in y_data_2],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="新增无症状感染者",
            y_axis=[int(i) for i in y_data_3],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="本土新增无症状感染者",
            y_axis=[int(i) for i in y_data_4],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="新增死亡",
            y_axis=[int(i) for i in y_data_5],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="新增治愈",
            y_axis=[int(i) for i in y_data_6],
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
        .render("../view/两月内每日新增.html")
    )

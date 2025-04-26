from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, PictorialBar
from pyecharts.globals import ThemeType, SymbolType
import provinces_process_data

df1 = provinces_process_data.get_confirmAdd(10)
df2 = provinces_process_data.get_confirm(10)
df3 = provinces_process_data.get_nowConfirm(10)
df4 = provinces_process_data.get_wzz_add(10)


def draw_confirm_add_bar():
    c = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(df1['name'].values.tolist())
            .add_yaxis("新增确诊", df1['confirmAdd'].values.tolist())
            .set_global_opts(
            title_opts={"text": "新增确诊Top10省份"}
        )
            .render("../view/前十省份新增确诊柱状图.html")
    )


def draw_confirm_add_pie():
    c = (
        Pie()
            .add("", [list(z) for z in zip(df1['name'].values.tolist(), df1['confirmAdd'])])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="新增确诊Top10省份"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left='90%', orient="vertical")
        )
            .set_series_opts(
            abel_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )

    c.render("../view/前十省份新增确诊饼图.html")


def draw_confirm_bar():
    c = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(df2['name'].values.tolist())
            .add_yaxis("累计确诊", df2['confirm'].values.tolist())
            .set_global_opts(
            title_opts={"text": "累计确诊Top10省份"}
        )
            .render("../view/前十省份累计确诊柱状图.html")
    )


def draw_confirm_pie():
    c = (
        Pie()
            .add("", [list(z) for z in zip(df2['name'].values.tolist(), df2['confirm'])])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="累计确诊Top10省份"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left='90%', orient="vertical")
        )
            .set_series_opts(
            abel_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )

    c.render("../view/前十省份累计确诊饼图.html")


def draw_now_confirm_bar():
    c = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(df3['name'].values.tolist())
            .add_yaxis("现存确诊", df3['nowConfirm'].values.tolist())
            .set_global_opts(
            title_opts={"text": "现存确诊Top10省份"}
        )
            .render("../view/前十省份现存确诊柱状图.html")
    )


def draw_now_confirm_pie():
    c = (
        Pie()
            .add("", [list(z) for z in zip(df3['name'].values.tolist(), df3['nowConfirm'])])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="现存确诊Top10省份"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left='90%', orient="vertical")
        )
            .set_series_opts(
            abel_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )

    c.render("../view/前十省份现存确诊饼图.html")


def draw_wzz_add_bar():
    c = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(df4['name'].values.tolist())
            .add_yaxis("新增无症状", df4['wzz_add'].values.tolist())
            .set_global_opts(
            title_opts={"text": "新增无症状Top10省份"}
        )
            .render("../view/前十省份新增无症状柱状图.html")
    )


def draw_wzz_add_pie():
    c = (
        Pie()
            .add("", [list(z) for z in zip(df4['name'].values.tolist(), df4['wzz_add'])])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="新增无症状Top10省份"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left='90%', orient="vertical")
        )
            .set_series_opts(
            abel_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )

    c.render("../view/前十省份新增无症状饼图.html")


def draw_confirm_add_picbar():
    c = (
        PictorialBar()
        .add_xaxis(df1['name'].values.tolist())
        .add_yaxis(
            "",
            df1['confirmAdd'].values.tolist(),
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=18,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],
            is_symbol_clip=True,
            symbol=SymbolType.ROUND_RECT,
        )
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="前十省份新增确诊"),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
        .render("../view/前十省份新增确诊象型柱状图.html")
    )

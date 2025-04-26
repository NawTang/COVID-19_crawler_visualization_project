from pyecharts.charts import Bar, Pie
from pyecharts.globals import ThemeType
from pyecharts import options as opts
import cities_process_data

df1 = cities_process_data.get_confirmAdd(10)
df2 = cities_process_data.get_confirm(10)
df3 = cities_process_data.get_nowConfirm(10)


def draw_confirm_add_bar():
    c = (
        Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(df1['city'].values.tolist())
        .add_yaxis("新增确诊", df1['confirmAdd'].values.tolist())
        .set_global_opts(
            title_opts={"text": "新增确诊Top10城市（区）"}
        )
        .render("../view/前十城市(区)新增确诊柱状图.html")
    )


def draw_confirm_add_pie():
    c1 = (
        Pie()
        .add("", [list(z) for z in zip(df1['city'].values.tolist(), df1['confirmAdd'])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="新增确诊Top10城市（区）"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left='90%', orient="vertical")
        )
        .set_series_opts(
            abel_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )

    c1.render("../view/前十城市(区)新增确诊饼图.html")


def draw_confirm_bar():
    c = (
        Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(df2['city'].values.tolist())
        .add_yaxis("累计确诊", df2['confirm'].values.tolist())
        .set_global_opts(
            title_opts={"text": "累计确诊Top10城市（区）"}
        )
        .render("../view/前十城市(区)累计确诊柱状图.html")
    )


def draw_confirm_pie():
    c = (
        Pie()
        .add("", [list(z) for z in zip(df2['city'].values.tolist(), df2['confirm'])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="累计确诊Top10城市（区）"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left='90%', orient="vertical")
        )
        .set_series_opts(
            abel_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )

    c.render("../view/前十城市(区)累计确诊饼图.html")


def draw_now_confirm_bar():
    c = (
        Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(df3['city'].values.tolist())
        .add_yaxis("现存确诊", df3['nowConfirm'].values.tolist())
        .set_global_opts(
            title_opts={"text": "现存确诊Top10城市（区）"}
        )
        .render("../view/前十城市(区)现存确诊柱状图.html")
    )


def draw_now_confirm_pie():
    c = (
        Pie()
        .add("", [list(z) for z in zip(df3['city'].values.tolist(), df3['nowConfirm'])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="现存确诊Top10城市（区）"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left='90%', orient="vertical")
        )
        .set_series_opts(
            abel_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )

    c.render("../view/前十城市(区)现存确诊饼图.html")

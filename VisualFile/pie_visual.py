from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd

df = pd.read_csv('../data_top10.csv', encoding='utf-8')

c1 = (
    Pie()
    .add("", [list(z) for z in zip(df['area'].values.tolist(), df['confirmedRelative'])])
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple", "#e34", "black", "gray"])
    .set_global_opts(title_opts=opts.TitleOpts(title="新增人数Top10"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)


c1.render("../view/pie_set_color.html")


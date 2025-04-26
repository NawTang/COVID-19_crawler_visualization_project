from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
import pandas as pd

df = pd.read_csv('../data_top10.csv', encoding='utf-8')
c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(df['area'].values.tolist())
    .add_yaxis("确诊人数", df['curConfirm'].values.tolist())
    .add_yaxis("新增人数", df['confirmedRelative'].values.tolist())
    .set_global_opts(
        title_opts={"text": "疫情Top10", "subtext": "展示了确诊人数和新增人数"}
    )
    .render("../view/bar_base_dict_config.html")
)

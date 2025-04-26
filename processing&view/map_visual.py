from pyecharts import options as opts
from pyecharts.charts import Map
import provinces_process_data


df = provinces_process_data.get_all()



def draw_confirmAdd_map():
    confirmAdd_map = (
        Map()
        .add('新增确诊', [list(i) for i in zip(df['name'].values.tolist(), df['confirmAdd'])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title='各地区新增确诊人数'),
            visualmap_opts=opts.VisualMapOpts(max_=20, is_inverse=True)
        )
        .render('../view/新增地图.html')
    )


def draw_confirm_map():
    confirm_map = (
        Map()
        .add('累计确诊', [list(i) for i in zip(df['name'].values.tolist(), df['confirm'])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title='各地区累计确诊人数'),
            visualmap_opts=opts.VisualMapOpts(max_=1000, is_inverse=True)
        )
        .render('../view/累计确诊地图.html')
    )


def draw_nowConfirm_map():
    nowConfirm_map = (
        Map()
        .add('现存确诊', [list(i) for i in zip(df['name'].values.tolist(), df['nowConfirm'])])
        .set_global_opts(
            title_opts=opts.TitleOpts(title='各地区现存确诊人数'),
            visualmap_opts=opts.VisualMapOpts(max_=200, is_inverse=True)
        )
        .render('../view/现存确诊地图.html')
    )


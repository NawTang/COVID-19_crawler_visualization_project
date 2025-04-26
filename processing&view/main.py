import add_line_visual
import add_rate_line_visual
import all_line_visual
import all_rate_line_visual
import cities_visual
import provinces_visual
import map_visual


if __name__ == '__main__':
    add_line_visual.draw()
    add_rate_line_visual.draw()
    all_line_visual.draw()
    all_rate_line_visual.draw()
    cities_visual.draw_confirm_add_pie()
    cities_visual.draw_now_confirm_pie()
    cities_visual.draw_confirm_add_bar()
    cities_visual.draw_confirm_bar()
    cities_visual.draw_confirm_pie()
    cities_visual.draw_now_confirm_bar()
    provinces_visual.draw_confirm_add_pie()
    provinces_visual.draw_now_confirm_pie()
    provinces_visual.draw_now_confirm_bar()
    provinces_visual.draw_confirm_pie()
    provinces_visual.draw_confirm_bar()
    provinces_visual.draw_confirm_add_bar()
    provinces_visual.draw_wzz_add_bar()
    provinces_visual.draw_wzz_add_pie()
    map_visual.draw_confirm_map()
    map_visual.draw_confirmAdd_map()
    map_visual.draw_nowConfirm_map()
    print('绘制完成！')

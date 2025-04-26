# coding:utf8

import requests
import store_to_csv
import store_in_mysql

headers = {
    'usr-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare'


def crawler():
    re = requests.post(url=url, headers=headers)
    dic = re.json()['data']
    day_add_list = dic['chinaDayAddList']
    day_all_list = dic['chinaDayList']
    data_list1 = []
    data_list2 = []
    # print(city_list)
    for da in day_add_list:
        # date = city['date']
        # localConfirmadd = city['localConfirmadd']
        # confirm = city['confirm']
        # infect = city['infect']
        dic = {'日期': da['date'], '本土新增确诊': da['localConfirmadd'], '新增确诊': da['confirm'],
               '新增无症状感染者': da['infect'], '新增死亡': da['dead'], '新增治愈': da['heal'],
               '本土新增无症状感染者': da['localConfirmadd'], '当日治愈率': da['healRate'], '当日死亡率': da['deadRate']}
        data_list1.append(dic)

    for da in day_all_list:
        # date = da['date']
        # localConfirm = da['localConfirm']
        # heal = da['heal']
        dic = {'日期': da['date'], '本土确诊': da['localConfirm'], '确诊': da['nowConfirm'],
               '治愈': da['heal'], '死亡': da['dead'],
               '总治愈率': da['healRate'], '总死亡率': da['deadRate']}
        data_list2.append(dic)

    store_to_csv.to_csv(data_list1, 'day_add_data')
    store_to_csv.to_csv(data_list2, 'day_all_data')
    store_in_mysql.store_to_day_add_data(data_list1)
    store_in_mysql.store_to_day_all_data(data_list2)


if __name__ == '__main__':
    crawler()

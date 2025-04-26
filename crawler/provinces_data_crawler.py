# coding:utf8

import requests
import store_to_csv
import store_in_mysql

headers = {
    'usr-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
c_url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,' \
        'chinaDayAddList,nowConfirmStatis,provinceCompare'


def crawler():
    re = requests.post(url=url, headers=headers)
    re2 = requests.post(url=c_url, headers=headers)
    dic = re.json()['data']
    provinces = dic['diseaseh5Shelf']['areaTree'][0]['children']
    compare_list = re2.json()['data']['provinceCompare']
    data_list = []
    # print(provinces)
    for province in provinces:
        # name = province['name']
        # newConfirm = province['today']['confirm']   # 新增
        # nowConfirm = province['total']['nowConfirm']    #现存确诊
        # confirm = province['total']['confirm']  # 累计确诊
        dic = {'name': province['name'], 'confirmAdd': province['today']['confirm'], 'wzz_add': province['today']['wzz_add'],
               'deadAdd': compare_list[province['name']]['dead'], 'healAdd': compare_list[province['name']]['heal'],
               'nowConfirm': province['total']['nowConfirm'], 'confirm': province['total']['confirm'],
               'heal': province['total']['heal'], 'dead': province['total']['dead'], 'wzz': province['total']['wzz'],
               'mediumRiskAreaNum': province['total']['mediumRiskAreaNum'],
               'highRiskAreaNum': province['total']['highRiskAreaNum']}
        data_list.append(dic)
    store_to_csv.to_csv(data_list, 'provinces_data')
    store_in_mysql.store_to_provinces_data(data_list)



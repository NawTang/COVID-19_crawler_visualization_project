# coding:utf8

import requests
import store_to_csv
import store_in_mysql

headers = {
    'usr-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryConfirmAdd,WomWorld,WomAboard'


def crawler():
    re = requests.post(url=url, headers=headers)
    dic = re.json()['data']
    country_list = dic['WomAboard']
    data_list = []
    for country in country_list:
        # name = country['name']
        # confirmAdd = country['confirmAdd']
        # nowConfirm = country['nowConfirm']
        dic = {'name': country['name'], 'continent': country['continent'], 'confirmAdd': country['confirmAdd'],
               'nowConfirm': country['nowConfirm'], 'confirm': country['confirm'],
               'deadCompare': country['deadCompare'], 'healCompare': country['healCompare']}
        data_list.append(dic)
    store_to_csv.to_csv(data_list, 'world_data')
    store_in_mysql.store_to_world_data(data_list)


# coding:utf8

import requests
import store_to_csv
import store_in_mysql

headers = {
    'usr-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf\\'


def crawler():
    re = requests.post(url=url, headers=headers)
    dic = re.json()['data']
    city_list = dic['statisGradeCityDetail']
    # print(city_list)
    data_list = []
    for city in city_list:
        dic = {'province': city['province'], 'city': city['province']+'-'+city['city'], 'confirm': city['confirm'],
               'nowConfirm': city['nowConfirm'], 'confirmAdd': city['confirmAdd']}
        data_list.append(dic)
    store_to_csv.to_csv(data_list, 'cities_data')
    store_in_mysql.store_to_cities_data(data_list)


if __name__ == '__main__':
    crawler()

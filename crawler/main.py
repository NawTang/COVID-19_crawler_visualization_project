import cities_data_crawler
import day_data_crawler
import provinces_data_crawler
import world_data_crawler


if __name__ == '__main__':
    print('正在获取城市疫情信息。。。')
    cities_data_crawler.crawler()
    print('正在获取每日疫情信息。。。')
    day_data_crawler.crawler()
    print('正在获取各省疫情信息。。。')
    provinces_data_crawler.crawler()
    print('正在获取世界疫情信息。。。')
    world_data_crawler.crawler()
    print('获取完成！')

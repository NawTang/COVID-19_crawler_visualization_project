import csv
import json

import requests
import re

# 伪装
headers = {
    # 浏览器
    'usr-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["area", "curConfirm", "confirmedRelative", "confirmed", "crued", "died"])
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
# 发送请求
response = requests.get(url=url, headers=headers)
# 获取数据
# print(response)       参数200表示获取成功
data_html = response.text
# 解析数据 "component":[内容]
# 在网页源代码当中匹配符合某一规则的一串数据
json_str = re.findall('"component":\[(.*)\],',data_html)[0]
# 类型转换 json字符串转成python字典类型
# python 数据容器{'key': 'value'}   json_dict['key']
json_dict = json.loads(json_str)
caseList = json_dict['caseList']
for case in caseList:
    area = case['area']
    confirmed = case['confirmed']   # 累计确诊
    confirmedRelative = case['confirmedRelative']   # 新增人数
    curConfirm = case['curConfirm']     # 确诊人数
    died = case['died']     # 累计死亡
    crued = case['crued']   # 累计治愈
    print(area, ":", confirmed, ",", curConfirm, ",", confirmedRelative, ",", crued, ",", died)
    with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([area, curConfirm, confirmedRelative, confirmed, crued, died])

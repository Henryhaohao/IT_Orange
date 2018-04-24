# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/3/25--13:55
__author__ = 'Henry'

'''
内容:爬取IT桔子中公司标签分类
目标网址:http://radar.itjuzi.com/company
'''

import requests
from bs4 import BeautifulSoup

url = 'http://radar.itjuzi.com/company'
#需要登录的cookie
head = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'gr_user_id=f4e1ff74-cca6-4f8b-8455-6201b8b952f6; acw_tc=AQAAANAfFgVfnQEA6krX31zNMf57uigb; identity=1073064953%40qq.com; remember_code=hBezMtQFUE; unique_token=529615; paidtype=vip; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1521860671; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1521950090; session=c8bf1e4c0aee0596cfc36e65e9fb92e870b2ac6c; user-radar.itjuzi.com=%7B%22n%22%3A%22%5Cu6854%5Cu53cb3c38bf2e9843e%22%2C%22v%22%3A2%7D; gr_session_id_eee5a46c52000d401f969f4535bdaa78=5331ade4-7812-4b73-ba7e-c505537aaaa8; gr_cs1_5331ade4-7812-4b73-ba7e-c505537aaaa8=user_id%3A529615; Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b=1521860750; Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b=1521955860; _ga=GA1.2.1041203472.1521860671; _gid=GA1.2.1400073980.1521860671; _gat=1; MEIQIA_EXTRA_TRACK_ID=12FqHHK1WnlIgT0BMyeZvSNMFjh',
    'Referer':'http://radar.itjuzi.com/company',
    'Host':'radar.itjuzi.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
html = requests.get(url,headers=head).text
soup = BeautifulSoup(html,'lxml')
#7个标签分类 (倒数第二个tag是搜索标签,要去掉)
tag = []
for i in soup.select('.filter-options-box > li > span > em'):
    tag.append(i.text)
tag.remove('TAG')
print(tag)
#子标签
tag_sub = []
for i in soup.select('.filter-box > ul > li > ul > li > a'):
        tag_sub.append(i.text)
print(tag_sub)

# tag_sub = []
# for i in soup.select('.filter-options-box > li > ul '):
#         a = list(i.stripped_strings) #.remove('')
#         tag_sub.append(a)
# print(tag_sub)

#子子标签(只有行业标签有)
tag_detail = []
for i in soup.select('.filter-box > ul > li:nth-of-type(1) > ul > li > ul > li > a'):
    if i.text != '全部':
        tag_detail.append(i.text)
print(tag_detail)








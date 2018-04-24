# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/3/25--13:10
__author__ = 'Henry'

'''
内容:爬取IT桔子中的各大公司详情
目标网址:http://radar.itjuzi.com/company
'''

import requests,time,re,random
import pymongo

client = pymongo.MongoClient('localhost',27017)
Henry = client['Henry']
IT_orange = Henry['IT_orange']

def spider(page): #要下载到第page页
    for i in range(1,page+1):
        url = 'http://radar.itjuzi.com/company/infonew?page={}'.format(str(i))
        #必须带上cookie才行
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
        html = requests.get(url,headers=head).json()
        # print(html)
        company = html['data']['rows']
        # print(company)
        for i in company:
            data = {
                'com_name': i['com_name'].replace('.',''),  # 公司名称
                'com_id': i['com_id'] , # 公司ID (公司详情页就是https://www.itjuzi.com/company/32756882; 最后是ID)
                'com_logo_archive': i['com_logo_archive'],  # 公司logo
                'com_born_date': i['com_born_date'],  # 成立时间
                'com_addr':i['com_addr'],  # 地区
                'com_des': i['com_des'].strip().replace('\r\n',''),  # 公司详情
                'com_cat_name': i['com_cat_name'],  # 行业
                'com_sub_cat_name':i['com_sub_cat_name'],  # 子行业
                'com_status': i['com_status'],  # 运营状态
                'com_fund_needs_name': i['com_fund_needs_name'],  # 是否需要融资
                'invse_date': i['invse_date'],  # 最新融资情况-日期
                'invse_round_id': i['invse_round_id'], # 最新融资情况-融资阶段(获投状态)(天使轮,A轮...)
                'invse_detail_money': i['invse_detail_money'],  # 最新融资情况-融资额
                'invse_total_money': i['invse_total_money'],  # 融资总额
                'com_scale': i['com_scale'],  # 规模
                'com_news_count': i['com_news_count'],  # 新闻数量
                'guzhi': i['guzhi'],  # 估值
            }
            print(data)
            try:
                IT_orange.insert_one(data)
            except:
                print('此数据已存在!')


# spider(6793)
# spider(1) --2018-3-26更新6条数据

#重新爬取公司名称(将公司名补全)并更新数据库
#需要代理IP
proxy_list = [
    '174.32.129.110:87'
]
proxy_ip = {'http':random.choice(proxy_list)}

def update_name():
    for i in IT_orange.find({}).limit(20):
        url = 'https://www.itjuzi.com/company/' + str(i['com_id'])
        # print(url)
        head = {
            'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host':'www.itjuzi.com',
            'Pragma': 'no-cache',
            # 'Referer': 'https://www.itjuzi.com/company/32756882',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/55.0.2883.87Safari/537.36',
            # 'Cookie': 'acw_tc=AQAAABlzP3AYtgIA6krX3+NxgH5DHxDp; gr_user_id=f4e1ff74-cca6-4f8b-8455-6201b8b952f6; MEIQIA_EXTRA_TRACK_ID=12Frjvn0LntrvPWAlyP963SRxXA; identity=1073064953%40qq.com; remember_code=hBezMtQFUE; unique_token=529615; paidtype=vip; acw_sc__=5ab8687386c655ba3cc0ec80fb02de86fb4c184a; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1521860671; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1522034950; gr_session_id_eee5a46c52000d401f969f4535bdaa78=10d45579-1052-436f-9459-1ae14dca9ecf; _ga=GA1.2.1041203472.1521860671; _gid=GA1.2.1400073980.1521860671; session=c55d70c7c8d438fb402dc1ee1b0540f5d1033ede'
        }
        html = requests.get(url,headers=head,proxies=proxy_ip).text
        print(html)
        com_name = re.findall(r'<meta name="Keywords" content="(.*?),',html)[0]
        print(com_name)
        #修改数据库中的com_name
        try:
            IT_orange.update({'com_name':i['com_name']},{'$set':{'com_name':com_name}})
        except:
            print('此数据更新失败:' + i['com_name'])

        # time.sleep(2)
    # print('更新完成!')

# update_name()


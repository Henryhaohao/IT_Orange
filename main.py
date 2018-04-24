# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/3/25--17:55
__author__ = 'Henry'


from multiprocessing import Pool
from company_list import spider,update_name

# verson1:
# if __name__ == '__main__':
#     page = 6793
#     pool = Pool(processes=8)
#     pool.apply_async(spider(page)) #pool.apply_async(spider,args=(page,))
#     pool.close()
#     pool.join()
#     print('爬取完成!')


# 爬取的公司名不完整 : 悠逸游Tri...
#	<meta name="Keywords" content="悠逸游Tripedition, | IT桔子" />
# 先进到详情页(查询数据库id拼成url),爬取带...的公司名,其他完整的就不用爬了,看是不是101859个,是的话直接数据库替换原来的名称就行了!

#verson2:(更新公司名)
if __name__ == '__main__':
    pool = Pool(processes=16)
    pool.apply_async(update_name())
    pool.close()
    pool.join()
    print('更新完成!')

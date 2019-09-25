# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class GupiaoXinlangPipeline(object):
    # def open_spider(self, spider):
    #     self.file = open('/Users/admin/PycharmProjects/scrapy_learn/gupiao_xinlang/gupiao_xinlang/spiders/gupiao_xinlang.json', 'w')
    #
    # def process_item(self, item, spider):
    #     if len(item) > 0 :
    #         # 数据处理的主要方法，在这里面定义对数据的操作
    #         # 将item强转成字典
    #         dict_data = dict(item)
    #         # 将字典转换成json字符串
    #         str_data = json.dumps(dict_data, ensure_ascii=False) + ',\n'
    #         # 写入文件
    #         self.file.write(str_data)
    #
    #     return item
    #
    # # 在爬虫停止的时候清理一些事情
    # def close_spider(self, spider):
    #     self.file.close()


    def __init__(self):
        # connection database
        self.connect = pymysql.connect('localhost', 'root', '123456', 'gupiao', use_unicode=True, charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        gupiao_name = item['gupiao_name']
        gupiao_id = item['gupiao_id']
        date_info = item['date_info']
        opening_price = item['opening_price']
        high_price = item['high_price']
        closing_price = item['closing_price']
        low_price = item['low_price']
        total_volume = item['total_volume']
        total_price = item['total_price']

        sqlstr = "insert into gupiao_xinlang(gupiao_name,gupiao_id,date_info,opening_price,high_price,closing_price,low_price,total_volume,total_price) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (gupiao_name,gupiao_id,date_info,opening_price,high_price,closing_price,low_price,total_volume,total_price)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sqlstr)
        self.connect.commit()
        self.connect.close()
        return item
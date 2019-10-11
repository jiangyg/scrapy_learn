# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class QiugouxinxiPipeline(object):
    # def open_spider(self, spider):
    #     self.file = open('qiugouxinxi.csv', 'w')
    #
    # def process_item(self, item, spider):
    #     if len(item) > 0 :
    #         # 数据处理的主要方法，在这里面定义对数据的操作
    #         # 将item强转成字典
    #         dict_data = dict(item)
    #         # 将字典转换成json字符串
    #         # 写入文件
    #         self.file.write(dict_data['company_name']+"|"+dict_data['hangye']
    #                         +"|" + dict_data['address']+"|" + dict_data['web']
    #                         +"|" + dict_data['product']+"|" + dict_data['link']
    #                         +"|" + dict_data['mobile']+"|" + dict_data['phone']+"\n")
    #
    #     return item
    #
    # # 在爬虫停止的时候清理一些事情
    # def close_spider(self, spider):
    #     self.file.close()

    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
                insert into qiugouxinxi(company_name,hangye,address,web,product,link,mobile,phone)
                values (%s,%s,%s,%s,%s,%s,%s,%s)
            """
        self.cursor.execute(insert_sql, (item["company_name"], item["hangye"], item["address"], item["web"],
                                         item["product"], item["link"], item["mobile"],
                                         item["phone"]))

        self.conn.commit()
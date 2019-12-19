# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pymysql
from pymongo.errors import DuplicateKeyError

from .items import ChuanzhongItem

class ChuanzhongPipeline(object):
    # def open_spider(self, spider):
    #     self.file = open('chuanzhong.json', 'w')
    #
    # def process_item(self, item, spider):
    #     if len(item) > 0:
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

    # 存入mysql
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        insert_sql = """
                        insert into chuanzhong(id,address,city,email,mobile,phone,region,title,user_name)
                        values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        self.cursor.execute(insert_sql, (item["id"], item["address"],item["city"],item["email"],item["mobile"],
                                         item["phone"],item["region"],item["title"],item["user_name"]))

        self.conn.commit()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class LikusoPipeline(object):
    # 存入mysql
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', '123456', 'test', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        insert_sql = """
                        insert into likuso(address,mobile,phone,title,user_name)
                        values (%s,%s,%s,%s,%s)
                    """
        self.cursor.execute(insert_sql, (item["address"],item["mobile"],
                                         item["phone"],item["title"],item["user_name"]))

        self.conn.commit()

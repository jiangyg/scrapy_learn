# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from pymongo.errors import DuplicateKeyError

from .items import LianjiaItem
from .settings import MONGO
# from zspider.zpipeline import CommonPipeline

class LianjiaPipeline(object):

    # 存入 csv
    # def open_spider(self, spider):
    #     self.file = open('lianjia_ershoufang.csv', 'w')
    #
    # def process_item(self, item, spider):
    #     if len(item) > 0 :
    #         # 数据处理的主要方法，在这里面定义对数据的操作
    #         # 将item强转成字典
    #         dict_data = dict(item)
    #         # 将字典转换成json字符串
    #         # 写入文件
    #         self.file.write(dict_data['baidu_location']+dict_data['src_id']+"|"+dict_data['city']+"|"
    #                         +dict_data['community']+"|"+dict_data['community_id']+"|"+dict_data['title']+"|"
    #                         +dict_data['total_price']+"|"+dict_data['unit_price']+"|"+dict_data['room_type']+"|"
    #                         +dict_data['floor']+"|"+dict_data['room_area']+"|"+dict_data['room_structure']+"|"
    #                         +dict_data['room_toward']+"|"+dict_data['true_area']+"|"+dict_data['buliding_type']+"|"
    #                         +dict_data['decorate_info']+"|"+dict_data['elevator_door']+"|"+dict_data['property_year']+"|"
    #                         +dict_data['building_structure']+"|"+dict_data['trading_type']+"|"
    #                         +dict_data['last_trade_time']+"|"+dict_data['room_using']+"|"+dict_data['listed_time']+"|"
    #                         +dict_data['room_age_limit']+"|"+dict_data['belongs']+"|"+dict_data['mortgage_info']+"|"
    #                         +dict_data['_id']+"\n")
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
                   insert into lianjia_ershoufang(id,baidu_location,belongs,building_structure,buliding_type,city,
                   community,community_id,decorate_info,elevator_door,floor,last_trade_time,listed_time,mortgage_info,
                   property_year,room_age_limit,room_area,room_structure,room_toward,room_type,room_using,src_id,title,
                   total_price,trading_type,true_area,unit_price)
                   values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
               """
        self.cursor.execute(insert_sql, (item["_id"], item["baidu_location"], item["belongs"], item["building_structure"],
                                         item["buliding_type"], item["city"], item["community"],item["community_id"],
                                         item["decorate_info"], item["elevator_door"], item["floor"], item["last_trade_time"],
                                         item["listed_time"], item["mortgage_info"], item["property_year"],item["room_age_limit"],
                                         item["room_area"], item["room_structure"], item["room_toward"],item["room_type"],
                                         item["room_using"], item["src_id"], item["title"],item["total_price"],
                                         item["trading_type"], item["true_area"], item["unit_price"]
                                         ))

        self.conn.commit()


    # 存入mongodb
    # def __init__(self):
    #     self.client = pymongo.MongoClient(host=MONGO['host'], port=MONGO['port'])
    #     self.mongoDb=self.client[MONGO['db']]
    #
    # def process_item(self, item, spider):
    #     # if isinstance(item, LianjiaItem):
    #     try:
    #         self.mongoDb['kb_%s' % 'lianjia_xiaoqu_wf'].insert(dict(item))
    #     except DuplicateKeyError:
    #         pass
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo.errors import DuplicateKeyError

from .items import LianjiaItem
from .settings import MONGO
# from zspider.zpipeline import CommonPipeline
#

class LianjiaPipeline(object):
    def open_spider(self, spider):
        self.file = open('lianjia_ershoufang.csv', 'w')

    def process_item(self, item, spider):
        if len(item) > 0 :
            # 数据处理的主要方法，在这里面定义对数据的操作
            # 将item强转成字典
            dict_data = dict(item)
            # 将字典转换成json字符串
            # 写入文件
            self.file.write(dict_data['baidu_location']+item['src_id']+"|"+item['city']+"|"+item['community']+"|"+
                            item['community_id']+"|"+item['title']+"|"+item['total_price']+"|"+item['unit_price']+"|"+item['room_type']+
                            "|"+item['floor']+"|"+item['room_area']+"|"+item['room_structure']+"|"+item['room_toward']+"|"+item['true_area']+"|"+item['buliding_type']+"|"+item['decorate_info']+"|"+item['elevator_door']+"|"+
                            item['property_year']+"|"+item['building_structure']+"|"+item['trading_type']+"|"+item['last_trade_time']+"|"+item['room_using']+"|"+
                            item['listed_time']+"|"+item['room_age_limit']+"|"+item['belongs']+"|"+item['mortgage_info']+"|"+item['_id']+"\n")

        return item

    # 在爬虫停止的时候清理一些事情
    def close_spider(self, spider):
        self.file.close()


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
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Dianhua400JzPipeline(object):
    # define the fields for your item here like:
    def open_spider(self, spider):
        self.file = open('/Users/admin/PycharmProjects/scrapy_learn/dianhua_400jz/dianhua_400jz/spiders/url_data.json',
                         'w')

    def process_item(self, item, spider):
        if len(item) > 0:
            # 数据处理的主要方法，在这里面定义对数据的操作
            # 将item强转成字典
            dict_data = dict(item)
            # 将字典转换成json字符串
            str_data = json.dumps(dict_data, ensure_ascii=False) + ',\n'
            # 写入文件
            self.file.write(str_data)

        return item

    # 在爬虫停止的时候清理一些事情
    def close_spider(self, spider):
        self.file.close()

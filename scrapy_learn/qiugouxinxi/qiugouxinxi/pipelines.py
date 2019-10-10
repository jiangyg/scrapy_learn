# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiugouxinxiPipeline(object):
    def open_spider(self, spider):
        self.file = open('qiugouxinxi.csv', 'w')

    def process_item(self, item, spider):
        if len(item) > 0 :
            # 数据处理的主要方法，在这里面定义对数据的操作
            # 将item强转成字典
            dict_data = dict(item)
            # 将字典转换成json字符串
            # 写入文件
            self.file.write(dict_data['company_name']+"|"+dict_data['hangye']
                            +"|" + dict_data['address']+"|" + dict_data['web']
                            +"|" + dict_data['product']+"|" + dict_data['link']
                            +"|" + dict_data['mobile']+"|" + dict_data['phone']+"\n")

        return item

    # 在爬虫停止的时候清理一些事情
    def close_spider(self, spider):
        self.file.close()

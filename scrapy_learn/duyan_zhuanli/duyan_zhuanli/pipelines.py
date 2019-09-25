# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import DuyanZhuanliItem
import pymysql

class DuyanZhuanliPipeline(object):
    # def open_spider(self, spider):
    #     self.file = open('/Users/admin/PycharmProjects/scrapy_learn/duyan_zhuanli/duyan_zhuanli/duyan_zhuanli.json', 'w')
    #
    # def process_item(self, item, spider):
    #     if len(item) > 0 :
    #         dict_data = dict(item)
    #         str_data = json.dumps(dict_data, ensure_ascii=False) + ',\n'
    #         self.file.write(str_data)
    #
    #     return item
    #
    # # 在爬虫停止的时候清理一些事情
    # def close_spider(self, spider):
    #     self.file.close()

    def __init__(self):
        # connection database
        self.connect = pymysql.connect('localhost', 'root', '123456', 'test', use_unicode=True, charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        aid = item['aid']
        aid2 = item['aid2']
        pubNumber = item['pubNumber']
        pubNumber2 = item['pubNumber2']
        title = item['title']
        abs = item['abs']
        applicant = item['applicant']
        agencyName = item['agencyName']
        department = item['department']
        applDate = item['applDate']
        pubDate = item['pubDate']
        lprs = item['lprs']
        province = item['province']
        city = item['city']
        district = item['district']
        address = item['address']
        mainIpc = item['mainIpc']
        keywords = item['keywords']
        dbType = item['dbType']
        sortId = item['sortId']
        legalStatus = item['legalStatus']
        legalStatusTag = item['legalStatusTag']
        curApplicant = item['curApplicant']
        curAddress = item['curAddress']

        sqlstr = "insert into zhuanli(aid,aid2,pubNumber,pubNumber2,title,abs,applicant,agencyName,department,applDate,pubDate,lprs,province,city,district,address,mainIpc,keywords,dbType,sortId,legalStatus,legalStatusTag,curApplicant,curAddress) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (aid, aid2, pubNumber, pubNumber2, title, abs, applicant, agencyName, department, applDate,pubDate, lprs, province, city, district, address, mainIpc, keywords, dbType, sortId, legalStatus,legalStatusTag, curApplicant, curAddress)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sqlstr)
        self.connect.commit()
        self.connect.close()
        return item
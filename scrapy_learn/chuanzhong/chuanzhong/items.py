# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChuanzhongItem(scrapy.Item):
    # 传众 id
    id = scrapy.Field()
    # 标题（大多数标题是公司的名称）
    title = scrapy.Field()
    # 姓名
    user_name = scrapy.Field()
    # 电话
    phone = scrapy.Field()
    # 手机
    mobile = scrapy.Field()
    # email
    email = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 省
    # province = scrapy.Field()
    # 市
    city = scrapy.Field()
    # 区
    region = scrapy.Field()
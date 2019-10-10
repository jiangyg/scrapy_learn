# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiugouxinxiItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    hangye = scrapy.Field()
    address = scrapy.Field()
    web = scrapy.Field()
    product = scrapy.Field()
    link = scrapy.Field()
    mobile = scrapy.Field()
    phone = scrapy.Field()
    pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LikusoItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    mobile = scrapy.Field()
    title = scrapy.Field()
    user_name = scrapy.Field()
    pass

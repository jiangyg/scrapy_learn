# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tx009Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    qq = scrapy.Field()
    phone = scrapy.Field()
    telephone = scrapy.Field()
    addr = scrapy.Field()
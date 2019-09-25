# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class GupiaoXinlangItem(scrapy.Item):
    # define the fields for your item here like:
    gupiao_name = Field()
    gupiao_id = Field()
    date_info = Field()
    opening_price = Field()
    high_price = Field()
    closing_price = Field()
    low_price = Field()
    total_volume = Field()
    total_price = Field()
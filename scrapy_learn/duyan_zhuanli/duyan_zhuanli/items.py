# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class DuyanZhuanliItem(scrapy.Item):
    # define the fields for your item here like:
    aid = Field()
    aid2 = Field()
    pubNumber = Field()
    pubNumber2 = Field()
    title = Field()
    abs = Field()
    applicant = Field()
    agencyName = Field()
    classes = Field()
    department = Field()
    applDate = Field()
    pubDate = Field()
    lprs = Field()
    province = Field()
    city = Field()
    district = Field()
    address = Field()
    mainIpc = Field()
    keywords = Field()
    dbType = Field()
    lastDate = Field()
    sortId = Field()
    legalStatus = Field()
    legalStatusTag = Field()
    curApplicant = Field()
    curAddress = Field()
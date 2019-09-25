# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class LianjiaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    region = Field()
    area = Field()
    xiaoqu = Field()
    jian_zhu_nian_dai = Field()
    jian_zhu_type = Field()
    wu_ye_fei = Field()
    wu_ye_ming = Field()
    kai_fa_shang = Field()
    lou_dong_shu = Field()
    fang_wu_shu = Field()
    fu_jin_men_dian = Field()
    xiao_qu_unit_price = Field()

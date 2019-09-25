# -*- coding: utf-8 -*-
import scrapy
import math
from scrapy import Spider,Request
import re
from lxml import etree
import json
from urllib.parse import quote
from ..items import LianjiaSpiderItem

class LianjiaSpSpider(scrapy.Spider):
    name = 'lianjia_sp'
    allowed_domains = ['sh.lianjia.com']

    def start_requests(self):
        base_url = "https://sh.lianjia.com/xiaoqu/50110000"
        # for i in range(10000,20607,1):
        for i in range(1,10000,1):
            i = i+1
            if len(str(i)) == 1:
                i = "0000"+str(i)
            elif len(str(i)) == 2:
                i = "000"+str(i)
            elif len(str(i)) == 3:
                i = "00" + str(i)
            elif len(str(i)) == 4:
                i = "0" + str(i)
            else :
                i = str(i)

            yield scrapy.Request(url=base_url+i, callback=self.parse,dont_filter=True) #用来获取页码

    def parse(self, response):
        try:
            item = LianjiaSpiderItem()

            region = response.css('.xiaoquDetailbreadCrumbs a::text').extract()[2]
            item['region'] = region
            area = response.css('.xiaoquDetailbreadCrumbs a::text').extract()[3]
            item['area'] = area
            xiaoqu = response.css('.xiaoquDetailbreadCrumbs a::text').extract()[4]
            item['xiaoqu'] = xiaoqu
            jian_zhu_nian_dai = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[0]
            item['jian_zhu_nian_dai'] = jian_zhu_nian_dai
            jian_zhu_type = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[1]
            item['jian_zhu_type'] = jian_zhu_type
            wu_ye_fei = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[2]
            item['wu_ye_fei'] = wu_ye_fei
            wu_ye_ming = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[3]
            item['wu_ye_ming'] = wu_ye_ming
            kai_fa_shang = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[4]
            item['kai_fa_shang'] = kai_fa_shang
            lou_dong_shu = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[5]
            item['lou_dong_shu'] = lou_dong_shu
            fang_wu_shu = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[6]
            item['fang_wu_shu'] = fang_wu_shu
            fu_jin_men_dian = response.css(".xiaoquDescribe span.xiaoquInfoContent::text").extract()[7]
            item['fu_jin_men_dian'] = fu_jin_men_dian
            xiao_qu_unit_price = response.css("span.xiaoquUnitPrice::text").extract()[0]
            item['xiao_qu_unit_price'] = xiao_qu_unit_price
        except IndexError:
            print ("Error: IndexError set xiao_qu_unit_price = 0")
            item['xiao_qu_unit_price'] = 0

        yield item

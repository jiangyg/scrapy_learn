# -*- coding: utf-8 -*-
import scrapy


class QiyeSpSpider(scrapy.Spider):
    name = 'qiye_sp'
    allowed_domains = ['qiye.net/']
    start_urls = ['http://qiye.net//']

    def parse(self, response):
        pass

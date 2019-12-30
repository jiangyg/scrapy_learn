# -*- coding: utf-8 -*-

import re
import scrapy
from ..items import LikusoItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import cpca


class LikusoSpSpider(scrapy.Spider):
    name = 'likuso_sp'
    allowed_domains = ['likuso.com']

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "Hm_lvt_ed0aae9c6ce44666479a741a33916a66=1577071286,1577088434; Hm_lpvt_ed0aae9c6ce44666479a741a33916a66=1577100445",
        "Host": "www.likuso.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }

    def start_requests(self):
        base_url = "http://www.likuso.com/city3/"
        # for i in range(1,50000,1):
        for i in range(220000,320000, 1):
            i = str(i)
            url = base_url+i+".html"
            print(url)
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse, dont_filter=True)  # 用来获取页码

    def parse(self, response):
        item = LikusoItem()
        item['title'] = 'None'
        item['address'] = "None"
        item['user_name'] = "None"
        item['phone'] = "None"
        item['mobile'] = "None"
        print(len(response.xpath('/html/body/div[6]/div/ul/li')))
        for i in range(len(response.xpath('/html/body/div[6]/div/ul/li'))):
            i=i+1
            if '全称' in response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/span/text()").extract()[0]:
                item['title'] = response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/text()").extract()[0]
            if '地址' in response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/span/text()").extract()[0]:
                item['address'] = response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/text()").extract()[0]
            if '联系人' in response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/span/text()").extract()[0]:
                item['user_name'] = response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/text()").extract()[0]
            if '电话' in response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/span/text()").extract()[0]:
                item['phone'] = response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/text()").extract()[0]
            if '手机' in response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/span/text()").extract()[0]:
                item['mobile'] = response.xpath("/html/body/div[6]/div/ul/li[" + str(i) + "]/text()").extract()[0].replace('【','')

        yield item
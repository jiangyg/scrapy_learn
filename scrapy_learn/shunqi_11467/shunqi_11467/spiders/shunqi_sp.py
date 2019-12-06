# -*- coding: utf-8 -*-
import scrapy
from ..items import Shunqi11467Item


class ShunqiSpSpider(scrapy.Spider):
    name = 'shunqi_sp'
    allowed_domains = ['www.11467.com']


    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "UM_distinctid=16da989ec912db-0a3a739d31fad6-1d3d6b50-13c680-16da989ec92437; SMTKF_visitor_id_113180=215868227; SMTKF_visitor_id_113233 = 215868253;SMTKF_visitor_id_88282 = 215868261;SMTKF_visitor_id_4911 = 215868269;SMTKF_visitor_id_37141 = 215868286;Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208=1574406873,1575544996; Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208=1575545115",
        "Host": "www.11467.com",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }


    def start_requests(self):
        base_url = "http://www.11467.com/shanghai/co/"
        for i in range(1000000, 1161602, 1):
            i = str(i+1)
            url = base_url+i+".htm"
            print(url)
            yield scrapy.FormRequest(url=url, headers=self.headers,callback=self.parse,dont_filter=True) #用来获取页码


    def parse(self, response):
        item = Shunqi11467Item()
        if '地址' in response.css('.codl dt::text').extract()[0]:
            print(response.css('.codl dt::text').extract()[0])
            print(response.css('.codl dd::text').extract()[0])
            item['address'] = response.css('.codl dd::text').extract()[0]
        else:
            item['address'] = "未知地址"
        if '电话' in response.css('.codl dt::text').extract()[1]:
            print(response.css('.codl dt::text').extract()[1])
            print(response.css('.codl dd::text').extract()[1])
            item['phone'] = response.css('.codl dd::text').extract()[1]
        else:
            item['phone'] = "未知电话"
        if '人' in response.css('.codl dt::text').extract()[2] \
                or '经理' in response.css('.codl dt::text').extract()[2]\
                or '长' in response.css('.codl dt::text').extract()[2]:
            print(response.css('.codl dt::text').extract()[2])
            print(response.css('.codl dd::text').extract()[2])
            item['user_name'] = response.css('.codl dd::text').extract()[2]
        else:
            item['user_name'] = "未知用户名"
        if '手机' in response.css('.codl dt::text').extract()[3]:
            print(response.css('.codl dt::text').extract()[3])
            print(response.css('.codl dd::text').extract()[3])
            item['mobile'] = response.css('.codl dd::text').extract()[3]
        else:
            item['mobile'] = "未知手机号"
        if '名称' in response.css('.codl td::text').extract()[0]:
            print(response.css('.codl td::text').extract()[0])
            print(response.css('.codl td::text').extract()[1])
            item['com_name'] = response.css('.codl td::text').extract()[1]
        else:
            item['com_name'] = "未知公司名"

        yield item

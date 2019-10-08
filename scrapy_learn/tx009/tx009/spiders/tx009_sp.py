# -*- coding: utf-8 -*-
import scrapy
from ..items import Tx009Item

class Tx009SpSpider(scrapy.Spider):
    name = 'tx009_sp'
    allowed_domains = ['tx009.com']

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=de188dc6448964206e44ef00f1ef496e01569382966; UM_distinctid=16d6bb1c2192a2-0a1ec67b94f001-38607504-13c680-16d6bb1c21aa4; CNZZDATA5467073=cnzz_eid%3D1568388142-1569465420-http%253A%252F%252Fwww.tx009.com%252F%26ntime%3D1569465420; __tins__18209839=%7B%22sid%22%3A%201569573227452%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201569575027452%7D; __51cke__=; __51laig__=1; PHPSESSID=4363os4a9btss42rijo5ss8tf2",
        "Host": "www.tx009.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    }


    def start_requests(self):
        base_url = "http://www.tx009.com/a/"
        # for i in range(1666800, 1898810, 1):
        for i in range(1666800, 1666802, 1):
            i = str(i+1)
            url = base_url+i
            print(url)
            yield scrapy.Request(url=url, headers=self.headers,callback=self.parse,dont_filter=True) #用来获取页码



    def parse(self, response):
        item = Tx009Item()
        item['name'] = response.xpath('/html/body/div[6]/div[1]/div[9]/div/div[2]/div/div[2]/ul/li[1]/text()').extract()[1].replace('\r','').replace('\n','').replace('\t','')
        print(response.xpath('/html/body/div[6]/div[1]/div[9]/div/div[2]/div/div[2]/ul/li[2]/text()').extract())

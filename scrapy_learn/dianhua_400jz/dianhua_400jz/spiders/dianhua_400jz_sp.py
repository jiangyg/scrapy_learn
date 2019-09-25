# -*- coding: utf-8 -*-
import scrapy
from ..items import Dianhua400JzItem

class Dianhua400jzSpSpider(scrapy.Spider):
    name = 'dianhua_400jz_sp'
    allowed_domains = ['400jz.com']

    start_url = ["mianyang.400jz.com/b22807.html"]
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d9ed643222387f63814f464b97b6d80dd1569243074; zhichi=1; UM_distinctid=16d5e2d11a339a-0ffb7786bb5499-38607504-13c680-16d5e2d11a4251; JSESSIONID=69526AB5DC5971F5868F1EC0166795A7; CNZZDATA1277741995=1673470878-1569240333-null%7C1569245759; cityWeb=jn; cityId=128",
        "Host": "www.400jz.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    }


    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response.text())


    # def start_requests(self):
    #     base_url = "http://400jz.com/qiuzhi/p"
    #     for i in range(1435):
    #     # for i in range(1):
    #         i = str(i+1)
    #         yield scrapy.Request(url=base_url + i + "/", headers=self.headers, callback=self.parse, dont_filter=True)
    #
    #
    #
    # def parse(self, response):
    #     item = Dianhua400JzItem()
    #     for li in response.xpath('//*[@id="list"]/ul/li'):
    #         data_url = li.css('a::attr(href)').extract()[0][2:]
    #         item['url'] = data_url
    #         yield item


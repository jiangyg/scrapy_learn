# -*- coding: utf-8 -*-
import scrapy
from ..items import QiugouxinxiItem

class QiugouxinxiSpSpider(scrapy.Spider):
    name = 'qiugouxinxi_sp'
    allowed_domains = ['qiugouxinxi.net']
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "ASP.NET_SessionId=2l5oqj244bnjwwf3qhkczylx; Hm_lvt_0ad874967db98b94cd85a42f4352a7e1=1570591617; Hm_lpvt_0ad874967db98b94cd85a42f4352a7e1=1570601186",
        "Host": "www.qiugouxinxi.net",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    }

    def start_requests(self):
        base_url = "https://www.qiugouxinxi.net/gs-"
        # 20191009
        # for i in range(3893114, 4185818, 1):
        # for i in range(3793114, 3893114, 1):
        # for i in range(2693114, 3693114, 1):
        # for i in range(1693114, 2693114, 1):
        for i in range(2107639, 2693114, 1):
            i = str(i+1)
            url = base_url+i+".html"
            print(url)
            yield scrapy.Request(url=url, headers=self.headers,callback=self.parse,dont_filter=True) #用来获取页码


    def parse(self, response):
        item = QiugouxinxiItem()
        company_name = ''
        hangye = ''
        address = ''
        web = ''
        product = ''
        link = ''
        mobile = ''
        phone = ''

        item['company_name'] = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[2]/span[2]/text()').extract()[0]
        try :
            hangye = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[1]/a[1]/text()').extract()[0]
        except :
            hangye = 'error'

        try :
            address = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[3]/span[2]/text()').extract()[0]
        except :
            address = 'error'

        try :
            web = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[4]/span[2]/text()').extract()[0]
        except :
            web = 'error'

        try :
            product = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[5]/span[2]/text()').extract()[0]
        except :
            product = 'error'

        try :
            link = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[6]/span[1]/text()').extract()[0]
        except :
            link = 'error'

        try :
            mobile = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[6]/span[3]/text()').extract()[0].split('/')[0].strip()
        except :
            mobile = 'error'

        try :
            phone = response.xpath('/html/body/div[4]/div[2]/div[1]/ul[1]/li[6]/span[3]/text()').extract()[0].split('/')[1].strip()
        except :
            phone = 'error'

        item['hangye'] = hangye
        item['address'] = address
        item['web'] = web
        item['product'] = product
        item['link'] = link
        item['mobile'] = mobile
        item['phone'] = phone

        yield item
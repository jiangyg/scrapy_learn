# -*- coding: utf-8 -*-
import scrapy
from ..items import LiebiaoItem

class LiebiaoSpSpider(scrapy.Spider):
    name = 'liebiao_sp'
    allowed_domains = ['liebiao.com']

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "_uv_id=168567950733409373; default_city=797; site_4374182=1; site_4374183=1; site_4374181=1; site_4374180=1; site_4374179=1; site_4374178=1; site_4374177=1; site_4374100=1; site_4374000=1; site_4370000=1; site_4300000=1; site_4000000=1; site_2000000=1; site_3000000=1; site_2900000=1; site_2800000=1; site_5000000=1; site_6000000=1; site_6200000=1; site_6300000=1; site_6400000=1; site_6500000=1; site_1900000=1; site_1800000=1; site_1700000=1; site_1600000=1; site_1500000=1; site_1200000=1; site_1100000=1; site_1110000=1; site_1109000=1; site_1108000=1; site_1106000=1; site_1104000=1; site_1103000=1; site_1102000=1; site_1101000=1; site_1100001=1; site_1000021=1; site_1000051=1; site_1100002=1; site_1100003=1; site_1100004=1; site_1100005=1; site_1100006=1; site_1110006=1; site_1110001=1; site_1110002=1; site_1110003=1; site_1110004=1; site_1110007=1; site_1110077=1; site_1110877=1; site_1110977=1; site_1111977=1; Hm_lvt_8cb62a9dc3928278834021acb890d8a4=1569291406; cities_last_visited=797_1704_20; site_1120007=1; site_1130007=1; site_1140007=1; site_1150007=1; site_1100007=1; site_1200007=1; Hm_lvt_d1c8e5c1164dcc070ae572bcabfe773f=1569252809,1569253122,1569289211,1569292052; Hm_lpvt_8cb62a9dc3928278834021acb890d8a4=1569292133; _sch_art=362150437%7C516355954%7C514575717%7C521330242%7C503949572; site_6400001=1; site_6400002=1; site_6400003=1; Hm_lvt_5b9bd125215c5e0e72ec530ac7f98b19=1569292265; Hm_lpvt_5b9bd125215c5e0e72ec530ac7f98b19=1569292265; site_6400004=1; site_4400001=1; site_5400001=1; site_5400002=1; site_5400012=1; site_5400013=1; site_5400018=1; site_5400019=1; insert_cityandcate_record=654%2C1113; site_5400099=1; Hm_lvt_37dd54aef610930836823892596e65ea=1569303103; Hm_lpvt_37dd54aef610930836823892596e65ea=1569303103; Hm_lpvt_d1c8e5c1164dcc070ae572bcabfe773f=1569303103",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    }

    def start_requests(self):
        base_url = "shop.liebiao.com/"
        # 20190924
        # for i in range(5400001,5600012,1):
        # 20190924_2
        # for i in range(5200001, 5400000, 1):
        # 20190925_1
        # for i in range(5000004, 5200000, 1):
        # 20190925_2
        for i in range(4800000,5000000,1):
            i = str(i+1)
            url = 'http://'+ i +'.' +base_url
            print(url)
            yield scrapy.Request(url=url, headers=self.headers,callback=self.parse,dont_filter=True) #用来获取页码


    def parse(self, response):
        item = LiebiaoItem()

        # 蓝色底样式的页面
        type = response.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[5]/span[2]/a/text()').extract()[0]
        print(type)
        if '贷款' in type:
            pass
        else:
            item['phone'] = response.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[4]/span[2]/text()').extract()[0].replace('\t','').replace('\n','').replace('\r','')
            print(item['phone'])
            if len(item['phone']) == 11:
                yield item

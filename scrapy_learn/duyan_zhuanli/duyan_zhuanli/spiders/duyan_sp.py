# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DuyanZhuanliItem

class DuyanSpSpider(scrapy.Spider):
    name = 'duyan_sp'
    allowed_domains = ['www.uyanip.com']
    start_urls = ['https://api.duyandb.com/search/search/queryByExp']

    headers = {
        "Accept": "application/json",
        "Authorization": "",
        "Content-Type": "application/json",
        "Origin": "https://www.uyanip.com",
        "Referer": "https://www.uyanip.com/result?exp=KEYWORD:(jingzan)",
        "Sec-Fetch-Mode": "cors",
        "secret": "541314f52d5e0284f004e0ab5571d4ff",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "uuid": "6c6b9a03-1e4f-49bc-b63b-ede665882dd0"
    }

    payload = {"exp": "KEYWORD:(大数据) AND ZLLX:(OR 5 OR 4)", "un_exp": "", "sort": 0, "pageSize": 200, "page": 1, "highlight": "true"}

    def start_requests(self):
        for i in range(20):
            print(self.payload['page']+i)
            self.payload['page'] = self.payload['page']+i
            yield scrapy.Request(
                self.start_urls[0],
                method="POST",
                headers=self.headers,
                body=json.dumps(self.payload),
                callback=self.parse,
                dont_filter=True
            )

    def parse(self, response):
        decode_json = json.loads(response.text)
        for i in decode_json['data']['list']:

            item = DuyanZhuanliItem()

            item['aid'] = i['aid']
            item['aid2'] = i['aid2']
            item['pubNumber'] = i['pubNumber']
            item['pubNumber2'] = i['pubNumber2']
            item['title'] = i['title'].replace("<span style=\"color: #fa8a00\">","").replace("</span>","")
            item['abs'] = i['abs'].replace("<span style=\"color: #fa8a00\">","").replace("</span>","")
            item['applicant'] = i['applicant'].replace("<span style=\"color: #fa8a00\">","").replace("</span>","")
            item['agencyName'] = i['agencyName']
            item['classes'] = i['classes']
            item['department'] = i['department']
            item['applDate'] = str(i['applDate'])
            item['pubDate'] = str(i['applDate'])
            item['lprs'] = i['lprs']
            item['province'] = i['province']
            item['city'] = i['city']
            item['district'] = i['district']
            item['address'] = i['address']
            item['mainIpc'] = i['mainIpc']
            item['keywords'] = i['keywords']
            item['dbType'] = str(i['dbType'])
            item['lastDate'] = str(i['lastDate'])
            item['sortId'] = str(i['sortId'])
            item['legalStatus'] = str(i['legalStatus'])
            item['legalStatusTag'] = i['legalStatusTag']
            item["curApplicant"] = i['curApplicant']
            item["curAddress"] = i['curAddress']

            yield item
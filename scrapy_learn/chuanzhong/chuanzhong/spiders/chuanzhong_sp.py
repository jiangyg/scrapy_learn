# -*- coding: utf-8 -*-

import re
from ..items import ChuanzhongItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import cpca

empty_word = 'null'

class ChuanzhongSpSpider(CrawlSpider):
    name = 'chuanzhong_sp'
    start_urls = ['http://www.czvv.com/huangye/65718770.html']

    rules = (
        Rule(LinkExtractor(allow=r'huangye/\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ChuanzhongItem()
        all_info = response.xpath('//div[@class="col-sm-12"]')
        title_set = set()

        company_title = response.xpath('//div[@class="col-xs-12 col-sm-10"]/div[@class="col-sm-12 Title"]/h2/text()').extract_first()
        item['title'] = company_title
        title_set.add('title')

        for info in all_info:

            title = ''
            try:
                title = info.xpath('./div[@class="title"]').extract_first().strip()
            except AttributeError:
                pass

            if '联系方式' in title:
                contact_information = info.xpath('./div[@class="col-sm-12"]/span[@class="col-sm-6 form-group"]').extract()
                contact_information = (', '.join(contact_information)).strip().replace('\n', '')
                re_ls = re.compile('<span.*?class="col-sm-3 text-muted">(.*?)</span>(.*?)</span>').findall(contact_information)
                need_info = []
                for ni in re_ls:
                    if '网址' in ni[0]:
                        pass
                    elif '注册资金' in ni[0]:
                        pass
                    elif '传真' in ni[0]:
                        pass
                    elif '邮编' in ni[0]:
                        pass
                    else:
                        nw = ''.join(ni).replace('\n','').replace('\t','').replace('\r','')
                        need_info.append(nw)
                for info in need_info:
                    if '商铺' in info:
                        item['id'] = info.split('>')[1].split('.')[0]
                        title_set.add('id')
                    elif '联系人' in info:
                        item['user_name'] = info.replace('联系人：','')
                        title_set.add('user_name')
                    elif '电话' in info:
                        item['phone'] = info.replace('电话：','')
                        title_set.add('phone')
                    elif '手机' in info:
                        item['mobile'] = info.replace('手机：','')
                        title_set.add('mobile')
                    elif '邮箱' in info:
                        item['email'] = info.replace('邮箱：','')
                        title_set.add('email')
                    elif '地址' in info:
                        df = cpca.transform([info.replace('地址：', '').replace(' ','')],pos_sensitive=True, cut=False)
                        item['address'] = info.replace('地址：', '').replace(' ','')
                        # item['province'] = df['省'][0]
                        item['city'] = df['市'][0]
                        item['region'] = df['区'][0]
                        title_set.add('address')
                        title_set.add('province')
                        title_set.add('city')
                        title_set.add('region')

        title_all = {'id','title','user_name','phone','mobile','email','address','city','region'}
        title_null = title_all - title_set

        for n_t in title_null:
            item[n_t] = empty_word

        yield item
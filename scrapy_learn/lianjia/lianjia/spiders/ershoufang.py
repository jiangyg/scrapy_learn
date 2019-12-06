# -*- coding: utf-8 -*-
# Author: yoga
import re
import scrapy
from ..items import LianjiaErshoufangItem

class ErshoufangSpider(scrapy.Spider):
    name = 'lianjia_ershoufang'
    source = 'www.lianjia.com'
    remark = '二手房爬虫'
    periodic = True
    start_urls_dict = {
        # '上海': 'https://sh.lianjia.com/ershoufang/',
        '北京': 'https://bj.lianjia.com/ershoufang/',
        # '广州': 'https://gz.lianjia.com/ershoufang/',
        # '深圳': 'https://sz.lianjia.com/ershoufang/',
        # '杭州': 'https://hz.lianjia.com/ershoufang/',
        # '南京': 'https://nj.lianjia.com/ershoufang/',
        # '郑州': 'https://zz.lianjia.com/ershoufang/',
        # '东莞': 'https://dg.lianjia.com/ershoufang/',
        # '天津': 'https://tj.lianjia.com/ershoufang/',
        # '宁波': 'https://nb.lianjia.com/ershoufang/',
        # '成都': 'https://cd.lianjia.com/ershoufang/',
        # '无锡': 'https://wx.lianjia.com/ershoufang/',
        # '武汉': 'https://wh.lianjia.com/ershoufang/',
        # '沈阳': 'https://sy.lianjia.com/ershoufang/',
        # '苏州': 'https://su.lianjia.com/ershoufang/',
        # '西安': 'https://xa.lianjia.com/ershoufang/',
        # '重庆': 'https://cq.lianjia.com/ershoufang/',
        # '长沙': 'https://cs.lianjia.com/ershoufang/',
        # '青岛': 'https://qd.lianjia.com/ershoufang/',
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                     ' Chrome/71.0.3578.98 Safari/537.36',
        # 'Host':'hz.lianjia.com'
    }
    def start_requests(self):
        """
        开始页
        :return:
        """
        for city in self.start_urls_dict:
            url = self.start_urls_dict[city]
            meta = {'url': url, 'city': city}
            yield scrapy.Request(url=url, callback=self.parse_district, meta=meta, headers=self.headers)

    def parse_district(self, response):
        """
        解析上海各个区的url
        :param response:
        :return:
        """

        up_url = response.meta['url']
        # print('cate_urls:',response.url)
        # 正则匹配url
        # compile_rule = re.compile(r'"/ershoufang/([a-z]+/)"', re.S)
        compile_rule = re.compile(r'"/ershoufang/([a-z]+([0-9])?/)"', re.S)
        urls = re.findall(compile_rule, response.text)
        for url in urls:
            if '{' not in url:
                yield scrapy.Request(url=up_url + url[0], callback=self.parse_district, meta=response.meta)
        lis = response.css('li.clear.LOGCLICKDATA')
        for li in lis:
            community = li.css('div.houseInfo > a::text').extract()[0]
            try:
                community_id = self.re_number(li.css('div.houseInfo > a::attr(href)').extract()[0])[0]
            except:
                community_id = ''
            title = li.css('div.title > a::text').extract()[0].strip()
            total_price = li.css('div.totalPrice > span::text').extract()[0]+li.css('div.totalPrice::text').extract()[0]
            price_meters = li.css('div.unitPrice > span::text ').extract()[0]
            href = li.css('div.info > div.title >a::attr(href)').extract()[0]
            # self.pedis.sadd('lianjia_url',href)
            # print('com_url:',href)
            # district_name = li.css('div.positionInfo > a.district::text').extract()[0]
            # area = li.css('div.positionInfo > a.bizcircle::text').extract()[0]
            meta = {
                'community': community,'community_id':community_id,
                'title': title,'total_price':total_price,'price_meters':price_meters,
                'city':response.meta['city']
                    }
            yield scrapy.Request(url=href, callback=self.parse_content,meta=meta, headers=self.headers)
        # 翻页操作
        if '/pg' not in response.url:
            try:
                page = re.search('{"totalPage":(\d+)', response.text).group(1)
                next_url = up_url +re.search('page-url="/ershoufang/(\S+)"page-data=', response.text).group(1)
                for i in range(2, int(page) + 1):
                    yield scrapy.Request(url=next_url.format(page=i), callback=self.parse_district, meta=response.meta,
                                         headers=self.headers)
            except:
                pass
    def parse_content(self, response):
        """
        解析详情页数据
        :param response:
        :return:
        meta = {
                'community': community,'community_id':community_id,
                'title': title,'total_price':total_price,'price_meters':price_meters
                    }
        """
        item = LianjiaErshoufangItem()
        url = response.url
        base_infos = response.css('div.base > div.content >ul >li')
        room_type = ''
        floor = ''
        buliding_area = ''
        house_type = ''
        house_toward = ''
        true_area = ''
        buliding_type = ''
        decorate_info = ''
        is_decorate = ''
        elevator_door = ''
        property_year = ''
        building_structure = ''
        for xiaoqu_info in base_infos:
            label = xiaoqu_info.css('span.label::text').extract()[0]
            content = xiaoqu_info.css('li::text').extract()[0]
            if label == '房屋户型':
                room_type = content
            elif label == '所在楼层':
                floor = content
            elif label == '建筑面积':
                buliding_area = content
            elif label == '户型结构':
                house_type = content
            elif label == '套内面积':
                true_area = content
            elif label == '建筑类型':
                buliding_type = content
            elif label == '房屋朝向':
                house_toward = content
            elif label == '建筑结构':
                building_structure = content
            elif label == '装修情况':
                decorate_info = content
            elif label == '梯户比例':
                elevator_door = content
            elif label == '装配电梯':
                is_decorate = content
            elif label == '产权年限':
                property_year = content
            else:
                pass
        # 交易属性
        trading_infos = response.css('div.transaction >div.content >ul > li')
        trading_type = ''
        up_time = ''
        house_using = ''
        listed_time = ''
        house_time = ''
        chanquan_belong = ''
        mortgage_info = ''
        house_attr = ''
        for trading_info in trading_infos:
            label = trading_info.css('span.label::text').extract()[0]
            content = trading_info.css('span:nth-child(2)::text').extract()[0]
            if label == '挂牌时间':
                listed_time = content
            elif label == '交易权属':
                trading_type = content
            elif label == '上次交易':
                up_time = content
            elif label == '房屋用途':
                house_using = content
            elif label == '房屋年限':
                house_time = content
            elif label == '产权所属':
                chanquan_belong = content
            elif label == '抵押信息':
                mortgage_info = content
            elif label == '房本备件':
                house_attr = content
        compile_rule = re.compile(r"resblockPosition:'(\S+)", re.S)
        lng_lat =re.findall(compile_rule, response.text)
        city = response.meta['city']
        src_id = self.re_number(url)[0]
        item['baidu_location'] = lng_lat[0].replace('\',','')
        item['src_id'] = src_id
        item['city'] = city
        item['community'] = response.meta['community']
        item['community_id'] = response.meta['community_id'].replace('.','')
        item['title'] = response.meta['title']
        item['total_price'] = response.meta['total_price']
        item['unit_price'] = response.meta['price_meters']
        item['room_type'] = room_type
        item['floor'] = floor
        item['room_area'] = buliding_area
        item['room_structure'] = house_type
        item['room_toward'] = house_toward
        item['true_area'] = true_area
        item['buliding_type'] = buliding_type
        item['decorate_info'] = decorate_info
        # item['is_decorate'] = is_decorate
        item['elevator_door'] = elevator_door
        item['property_year'] = property_year
        item['building_structure'] = building_structure
        item['trading_type'] = trading_type
        item['last_trade_time'] = up_time
        item['room_using'] = house_using
        item['listed_time'] = listed_time
        item['room_age_limit'] = house_time
        item['belongs'] = chanquan_belong
        item['mortgage_info'] = mortgage_info.strip()
        # item['house_attr'] = house_attr
        item['_id'] = src_id
        yield item

    def re_number(self, string):
        '''
        正则取数字
        '''
        return re.findall(r"\d+\.?\d*", string)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    management_fee = scrapy.Field()  # 物业费
    baidu_location = scrapy.Field()  # 百度经纬度
    address = scrapy.Field()  # 地址
    finish_time = scrapy.Field()  # 建成时间
    developer = scrapy.Field()  # 开发商
    city = scrapy.Field()  # 市
    src_id = scrapy.Field()  # 数据id
    district = scrapy.Field()  # 区
    src_site = scrapy.Field()  # 来源网站
    total_room = scrapy.Field()  # 总户数
    name = scrapy.Field()  # 名称
    building_type = scrapy.Field()  # 建筑类型
    price = scrapy.Field()  # 单价
    management_company = scrapy.Field()  # 物业公司
    total_building = scrapy.Field()  # 总楼栋数
    building_area = scrapy.Field()  # 总建筑面积,
    park_num = scrapy.Field()  # 车位数
    park_price = scrapy.Field()  # 车位租金
    gaode_location = scrapy.Field()  # 车位租金
    distance = scrapy.Field()  # 车位租金
    _id = scrapy.Field()


class LianjiaErshoufangItem(scrapy.Item):
    _id = scrapy.Field()
    room_type = scrapy.Field()  # 房屋结构
    buliding_type = scrapy.Field()  # 建筑类型
    belongs = scrapy.Field()  # 产权所属
    unit_price = scrapy.Field()  # 单价
    total_price = scrapy.Field()  # 总价
    room_toward = scrapy.Field()  # 房屋朝向
    trading_type = scrapy.Field()  # 交易权属
    elevator_door = scrapy.Field()  # 梯户比
    floor = scrapy.Field()  # 楼层
    listed_time = scrapy.Field()  # 挂牌时间
    room_area = scrapy.Field()  # 房屋建筑面积
    room_using = scrapy.Field()  # 房屋用途
    room_structure = scrapy.Field()  # 房间结构
    mortgage_info = scrapy.Field()  # 抵押信息
    community_id = scrapy.Field()  # 小区id
    community = scrapy.Field()  # 所属小区
    property_year = scrapy.Field()  # 产权年限
    true_area = scrapy.Field()  # 套内面积
    city = scrapy.Field()  # 市
    baidu_location = scrapy.Field()  # 百度经纬度
    last_trade_time = scrapy.Field()  # 上次交易时间
    building_structure = scrapy.Field()  # 建筑结构
    decorate_info = scrapy.Field()  # 装修情况
    src_id = scrapy.Field()  # 数据id
    src_site = scrapy.Field()  # 来源网站
    title = scrapy.Field()  # 挂牌名称
    room_age_limit = scrapy.Field()  # 房屋年限


class LianjiaZufangItem(scrapy.Item):
    title = scrapy.Field()
    district = scrapy.Field()
    region = scrapy.Field()
    src_id = scrapy.Field()
    src_site = 'lianjia'
    post_time = scrapy.Field()
    price = scrapy.Field()
    tags = scrapy.Field()
    rent_type = scrapy.Field()
    house_type = scrapy.Field()
    house_area = scrapy.Field()
    house_toward = scrapy.Field()
    live_time = scrapy.Field()
    rent_range = scrapy.Field()
    look_house = scrapy.Field()
    floor = scrapy.Field()
    elevator = scrapy.Field()
    parking_space = scrapy.Field()
    water = scrapy.Field()
    fuel_gas = scrapy.Field()
    electricity = scrapy.Field()
    lng_lat = scrapy.Field()
    city = scrapy.Field()
    _id = scrapy.Field()
    community = scrapy.Field()
    community_id = scrapy.Field()

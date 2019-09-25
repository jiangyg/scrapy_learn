# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import CanadaWeatherItem


class CanadaSpSpider(scrapy.Spider):
    name = 'canada_sp'
    allowed_domains = ['tianqihoubao.com']

    def start_requests(self):
        base_url = "http://www.tianqihoubao.com/guoji/"
        city_list = [2755,2756,2757,2758,2759,2760,2761,2762,2763,2764,2765,2766,2767,2768,2769,2770,2771,2772,2773,2774,2775,2776,2777,2778,2779,2780,2781,2782,2783,2784,2785,2786,2787,2788,2789,2790,2791,2792,2793,2794,2795,2796,2797,2798,2799,2800,2801,2802,2803,2804,2805,2806,2807,2808,2809,2810,2811,2812,2813,2814,2815,2816,2817,2818,2819,2820,2821,2822,2823,2824,2825,2826,2827,2828,2829,2830,2831,2832,2833,2834,2835,2836,2837,2838,2839,2840,2841,2842,2843,2844,2845,2846,2847,2848,2849,2850,2851,2852,2853,2854,2855,2856]
        # city_list = [2755]
        date_list = ["2013-11","2013-12","2014-1","2014-2","2014-3","2014-4","2014-5","2014-6","2014-7","2014-8","2014-9","2014-10","2014-11","2014-12","2015-1","2015-2","2015-3","2015-4","2015-5","2015-6","2015-7","2015-8","2015-9","2015-10","2015-11","2015-12","2016-1","2016-2","2016-3","2016-4","2016-5","2016-6","2016-7","2016-8","2016-9","2016-10","2016-11","2016-12","2017-1","2017-2","2017-3","2017-4","2017-5","2017-6","2017-7","2017-8","2017-9","2017-10","2017-11","2017-12","2018-1","2018-2","2018-3","2018-4","2018-5"]
        # date_list = ["2013-11"]
        for i in city_list:
            i = str(i)
            for j in date_list:
                yield scrapy.Request(url=base_url + i + "/" + j + ".html", callback=self.parse, dont_filter=True)
    def parse(self, response):
        print(response.status)
        name_res = r"<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>"
        item = CanadaWeatherItem()
        item['city'] = response.xpath('//*[@id="mnav"]/div[1]/a[4]/text()').extract()[0].replace('历史天气','')

        for data in response.css('table tr').extract():
            res = re.compile(name_res,re.S)
            data_t = re.findall(res,data)[0]
            data_list = list(data_t)
            if data_list[0].replace('\r\n', '').replace(' ','').startswith('20'):
                item['date'] = data_list[0].replace('\r\n', '').replace(' ','')
                item['weather'] = data_list[1].replace('\r\n', '').replace(' ', '')
                item['temperature'] = data_list[2].replace('\r\n', '').replace(' ', '')
                item['wind'] = data_list[3].replace('\r\n', '').replace(' ', '')
            else:
                pass

            if (item.__len__() == 5):
                yield item
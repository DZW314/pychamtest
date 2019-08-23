#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'DZW'
__mtime__ = '2019/8/22'
# code is far away from bugs with the god animal protecting
    I love animals. They are so funny. 
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   *   ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃ Bless ┣┓
              ┃ NoBUG ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from ..items import Test51JobItem
import re

class Music_menghua(CrawlSpider):
    name = "getdata"
    start_urls = ["http://www.hhimm.com/manhua/7688.html"]
    def parse(self, response):
        item = Test51JobItem()
        selector = Selector(response)
        Music_List = selector.css('#permalink .cVolList ul')
        print("33333333333",Music_List)
        for li in Music_List:
            music_name = li.xpath('li/text()').extract()
            music_link = li.xpath('li/a/@href').extract()
            print('33333333333')
            # 给item赋值
            item['music_name'] = music_name     # 名字
            item['music_link'] = music_link     # 链接
            yield item


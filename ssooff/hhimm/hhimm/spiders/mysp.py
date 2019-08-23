# -*- coding: utf-8 -*-
import scrapy
from ..items import HhimmItem

class MyspSpider(scrapy.Spider):
    name = 'mysp'
    allowed_domains = ['hhimm.com']
    start_urls = ['http://www.hhimm.com/manhua/7688.html']

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = HhimmItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item
        pass

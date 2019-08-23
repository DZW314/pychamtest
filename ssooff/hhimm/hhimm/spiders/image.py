# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import HhimmItem

class MyspSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['hhimm.com']
    start_urls =['http://www.hhimm.com/cool285611/2.html?s=6']
    rules = (
        Rule(LinkExtractor(allow=(''), restrict_xpaths=(u"//a[contains(text(),'下一页')]")), follow=True),
        Rule(LinkExtractor(allow=('http://www.hhimm.com/(.*?).html'), restrict_xpaths=(u"//div[@class='ABox']")),
             callback="parse", follow=False),
    )

    def parse(self, response):
        for sel in response.xpath('//img[id="img2391"]/src'):
            # item = HhimmItem()
            # yield item
            print(sel)
        pass
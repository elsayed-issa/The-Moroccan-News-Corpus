# -*- coding: utf-8 -*-
import scrapy


class KifSpider(scrapy.Spider):
    name = 'kif'
    allowed_domains = ['kifache.com']
    start_urls = ['http://kifache.com/']

    def parse(self, response):
        pass

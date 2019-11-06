# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class MaSpider(Spider):
    name = 'ma'
    allowed_domains = ['www.maghress.com']
    start_urls = ['https://www.maghress.com/politics']

    def parse(self, response):
        pass

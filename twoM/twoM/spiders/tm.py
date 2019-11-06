# -*- coding: utf-8 -*-
import scrapy


class TmSpider(scrapy.Spider):
    name = 'tm'
    allowed_domains = ['www.2m.ma/ar/']
    start_urls = ['http://www.2m.ma/ar//']

    def parse(self, response):
        pass

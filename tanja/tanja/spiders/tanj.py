# -*- coding: utf-8 -*-
import scrapy


class TanjSpider(scrapy.Spider):
    name = 'tanj'
    allowed_domains = ['tanja24.com']
    start_urls = ['http://tanja24.com/']

    def parse(self, response):
        pass

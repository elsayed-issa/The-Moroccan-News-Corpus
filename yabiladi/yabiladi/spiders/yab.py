# -*- coding: utf-8 -*-
import scrapy


class YabSpider(scrapy.Spider):
    name = 'yab'
    allowed_domains = ['ar.yabiladi.com']
    start_urls = ['http://ar.yabiladi.com/']

    def parse(self, response):
        pass

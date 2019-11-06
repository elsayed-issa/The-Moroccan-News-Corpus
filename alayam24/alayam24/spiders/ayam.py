# -*- coding: utf-8 -*-
import scrapy


class AyamSpider(scrapy.Spider):
    name = 'ayam'
    allowed_domains = ['www.alayam24.com']
    start_urls = ['http://www.alayam24.com/']

    def parse(self, response):
        pass

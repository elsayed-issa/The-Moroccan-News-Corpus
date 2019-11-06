# -*- coding: utf-8 -*-
import scrapy


class NadorSpider(scrapy.Spider):
    name = 'nador'
    allowed_domains = ['www.nadorcity.com']
    start_urls = ['http://www.nadorcity.com/']

    def parse(self, response):
        pass

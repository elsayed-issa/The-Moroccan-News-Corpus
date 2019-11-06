# -*- coding: utf-8 -*-
import scrapy


class AkhbarSpider(scrapy.Spider):
    name = 'akhbar'
    allowed_domains = ['www.akhbarona.com']
    start_urls = ['http://www.akhbarona.com/']

    def parse(self, response):
        pass

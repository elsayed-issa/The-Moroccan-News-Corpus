# -*- coding: utf-8 -*-
import scrapy


class TelegraphSpider(scrapy.Spider):
    name = 'telegraph'
    allowed_domains = ['maroctelegraph.com']
    start_urls = ['http://maroctelegraph.com/']

    def parse(self, response):
        pass

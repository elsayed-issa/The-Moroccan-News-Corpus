# -*- coding: utf-8 -*-
import scrapy


class TeleSpider(scrapy.Spider):
    name = 'tele'
    allowed_domains = ['telexpresse.com']
    start_urls = ['http://telexpresse.com/']

    def parse(self, response):
        pass

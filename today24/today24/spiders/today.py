# -*- coding: utf-8 -*-
import scrapy


class TodaySpider(scrapy.Spider):
    name = 'today'
    allowed_domains = ['www.alyaoum24.com']
    start_urls = ['http://www.alyaoum24.com/']

    def parse(self, response):
        pass

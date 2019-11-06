# -*- coding: utf-8 -*-
import scrapy


class MorcTodaySpider(scrapy.Spider):
    name = 'morc_today'
    allowed_domains = ['www.almaghribtoday.net']
    start_urls = ['http://www.almaghribtoday.net/']

    def parse(self, response):
        pass

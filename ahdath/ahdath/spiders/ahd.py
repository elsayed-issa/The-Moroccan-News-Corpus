# -*- coding: utf-8 -*-
import scrapy


class AhdSpider(scrapy.Spider):
    name = 'ahd'
    allowed_domains = ['ahdath.info']
    start_urls = ['http://ahdath.info/']

    def parse(self, response):
        pass

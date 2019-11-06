# -*- coding: utf-8 -*-
import scrapy


class DalilSpider(scrapy.Spider):
    name = 'dalil'
    allowed_domains = ['dalil-rif.com']
    start_urls = ['http://dalil-rif.com/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy


class FebSpider(scrapy.Spider):
    name = 'feb'
    allowed_domains = ['www.febrayer.com']
    start_urls = ['https://febrayer.com/category/politique',]

    def parse(self, response):
        content = response.xpath('//*[@class="single-content"]/p/text()').extract()
        yield{'content':content}

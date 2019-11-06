# -*- coding: utf-8 -*-
import scrapy


class BarSpider(scrapy.Spider):
    name = 'bar'
    allowed_domains = ['www.barlamane']
    start_urls = ['https://www.barlamane.com/%d9%85%d8%b9%d8%a7%d8%b1%d8%b6%d9%88-%d8%a8%d9%86%d8%b4%d9%85%d8%a7%d8%b4-%d9%8a%d8%ad%d8%af%d8%af%d9%88%d9%86-%d8%aa%d8%a7%d8%b1%d9%8a%d8%ae-%d8%a7%d9%84%d9%85%d8%a4%d8%aa%d9%85%d8%b1-%d8%a7%d9%84/']

    def parse(self, response):
        pass

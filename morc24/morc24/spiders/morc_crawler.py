# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Morc24Item
from scrapy.loader import ItemLoader


class MorcCrawlerSpider(CrawlSpider):
    name = 'morc_crawler'
    allowed_domains = ['www.almaghreb24.com']
    start_urls = ['https://almaghreb24.com/%D9%88%D8%B2%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D9%88%D8%B8%D9%8A%D9%81%D8%A9-%D8%AA%D9%86%D8%B4%D8%B1-%D8%AA%D9%82%D8%B1%D9%8A%D8%B1%D8%A7%D9%8B-%D8%AD%D9%88%D9%84-%D8%A7%D9%84%D8%A2%D8%AB%D8%A7%D8%B1/']

    rules = (
        Rule(LinkExtractor(allow=r'[^https:\/\/www.almaghreb\d..com.]'), callback='parse_item', follow=True),)

    def parse_item(self, response):
        #articles = response.xpath('//*[@class="entry-content clearfix"]')
        
        #for article in articles:
            item = Morc24Item()
            #item['title'] = response.xpath('//*[@class="main-content"]/div/article/header/h1/text()').extract_first()
            item['content'] = response.xpath('//*[@class="entry-content clearfix"]/p/span/strong/text()').extract()
            yield item
            

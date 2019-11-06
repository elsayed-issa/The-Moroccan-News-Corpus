# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Today24Item
from scrapy.loader import ItemLoader


class MorcCrawlerSpider(CrawlSpider):
    name = 'today_crawler'
    allowed_domains = ['www.alyaoum24.com']
    start_urls = ['http://www.alyaoum24.com/1265553.html']

    rules = (
        Rule(LinkExtractor(allow=r'^http:\/\/www.alyaoum24.com.'), callback='parse_item', follow=True),)

    def parse_item(self, response):
            item = Today24Item()
            item['content'] = response.xpath('//*[@id="post_content"]/p/text()').extract() 
            yield item
            

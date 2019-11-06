# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MaghresItem
from scrapy.loader import ItemLoader


class MaCrawlerSpider(CrawlSpider):
    name = 'ma_crawler'
    allowed_domains = ['www.maghress.com']
    start_urls = ['']

    rules = (
        Rule(LinkExtractor(allow=r'topics.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        articles = response.xpath('//*[@class="col-md-12"]')
        
        for article in articles:
            item = MaghresItem()
            #item['url'] = article.xpath('a[@class="read-more"]/@href').extract()
            #item['url'] = article.xpath('a[@class="read-more"]/text()').extract()
            item['title'] = article.xpath('//*[@class="col-md-12"]/h1/text()').extract_first() 
            item['content'] = article.xpath('//*[@class="col-md-12"]/div[@class="content"]/p/text()').extract()
            yield item

        next_page_url = response.xpath('//*[@class="col-md-12"]/a[@class="nav-btn left"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_item)

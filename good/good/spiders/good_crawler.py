# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import GoodItem
from scrapy.loader import ItemLoader


class GoodCrawlerSpider(CrawlSpider):
    name = 'good_crawler'
    allowed_domains = ['goud.ma']
    start_urls = ['https://www.goud.ma/topics/%D8%A2%D8%B4-%D9%88%D8%A7%D9%82%D8%B9/',
                  'https://www.goud.ma/topics/%D8%A2%D8%B1%D8%A7%D8%A1/',
                  'https://www.goud.ma/%D9%88%D9%81%D8%AF-%D8%B1%D8%B3%D9%85%D9%8A-%D8%BA%D8%A7%D8%AF%D9%8A-%D8%A7%D9%8A%D8%AC%D9%8A-%D9%81%D8%A7%D9%86%D8%B7%D9%84%D8%A7%D9%82%D8%A9-%D8%A3%D9%88%D9%84-%D8%B1%D8%AD%D9%84%D8%A9-%D8%AC%D9%88-458329/',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'topics.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        articles = response.xpath('//*[@class="col-md-12"]')
        
        for article in articles:
            item = GoodItem()
            #item['url'] = article.xpath('a[@class="read-more"]/@href').extract()
            #item['url'] = article.xpath('a[@class="read-more"]/text()').extract()
            item['title'] = article.xpath('//*[@class="col-md-12"]/h1/text()').extract_first() 
            item['content'] = article.xpath('//*[@class="col-md-12"]/div[@class="content"]/p/text()').extract()
            yield item

        next_page_url = response.xpath('//*[@class="col-md-12"]/a[@class="nav-btn left"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_item)

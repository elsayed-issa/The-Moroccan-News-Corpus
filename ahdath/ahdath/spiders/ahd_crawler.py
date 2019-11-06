# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AhdathItem
from scrapy.loader import ItemLoader


class GoodCrawlerSpider(CrawlSpider):
    name = 'ahd_crawler'
    allowed_domains = ['ahdath.info']
    start_urls = ['http://ahdath.info/494654']

    rules = (
        #Rule(LinkExtractor(allow=r'topics.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^^http:\/\/ahdath.info.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = AhdathItem()
            item['content'] = response.xpath('//*[@class="single-content"]/p/text()').extract()
            with open ('ahd2.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

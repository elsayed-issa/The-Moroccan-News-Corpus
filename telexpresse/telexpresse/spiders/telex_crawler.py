# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TelexpresseItem
from scrapy.loader import ItemLoader


class TelexCrawlerSpider(CrawlSpider):
    name = 'telex_crawler'
    allowed_domains = ['telexpresse.com']
    start_urls = ['http://telexpresse.com/permalink/108229.html']

    rules = (
        Rule(LinkExtractor(allow=r'permalink.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = TelexpresseItem()
            item['content'] = article.xpath('//*[@class="col-md-12"]/div[@class="content"]/p/text()').extract()
            yield item
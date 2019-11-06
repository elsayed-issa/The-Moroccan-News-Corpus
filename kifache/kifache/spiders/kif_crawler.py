# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import KifacheItem
from scrapy.loader import ItemLoader


class KifCrawlerSpider(CrawlSpider):
    name = 'kif_crawler'
    allowed_domains = ['kifache.com']
    start_urls = ['https://kifache.com/414668/']

    rules = (
        Rule(LinkExtractor(allow=r'\d.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = KifacheItem()
            item['content'] = response.xpath('//*[@class="single-content"]/p/text()').extract()
            with open('kif.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

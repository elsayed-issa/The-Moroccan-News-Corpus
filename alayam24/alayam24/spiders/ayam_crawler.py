# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Alayam24Item
from scrapy.loader import ItemLoader


class AyamCrawlerSpider(CrawlSpider):
    name = 'ayam_crawler'
    allowed_domains = ['www.alayam24.com']
    start_urls = ['https://www.alayam24.com/articles-73890.html']

    rules = (
        Rule(LinkExtractor(allow=r'articles.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = Alayam24Item()
            item['content'] = response.xpath('//*[@class="articlecontent"]/p/text()').extract()
            with open ('ayam.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item
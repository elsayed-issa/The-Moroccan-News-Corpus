# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DalilRifItem
from scrapy.loader import ItemLoader


class DalilCrawlerSpider(CrawlSpider):
    name = 'dalil_crawler'
    allowed_domains = ['dalil-rif.com']
    start_urls = ['https://dalil-rif.com/permalink/21075.html']

    rules = (
        Rule(LinkExtractor(allow=r'\d.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = DalilRifItem() 
            item['content'] = response.xpath('//*[@id="article_body"]/p/span/text()').extract()
            with open('dalil.txt','a') as f:
                f.write('content: [{0}\n'.format(item['content']))
            yield item

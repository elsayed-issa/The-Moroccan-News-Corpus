# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TwomItem
from scrapy.loader import ItemLoader


class TmCrawlerSpider(CrawlSpider):
    name = 'tm_crawler'
    allowed_domains = ['www.2m.ma/ar']
    start_urls = ['http://www.2m.ma/ar/news/%D9%85%D8%AF%D8%B1%D8%A8%D9%88%D9%86-%D9%88%D9%84%D8%A7%D8%B9%D8%A8%D9%88%D9%86-%D9%85%D8%B5%D8%B1%D9%8A%D9%88%D9%86-%D8%B3%D8%A7%D8%A8%D9%82%D9%88%D9%86-%D8%A3%D8%AF%D8%A7%D8%A1-%D8%A7%D9%84%D9%85%D9%86%D8%AA%D8%AE%D8%A8-%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8%D9%8A-%D8%B3%D9%8A%D8%AA%D8%AD%D8%B3%D9%86-%D9%81%D9%8A-%D9%82%D8%A7%D8%AF%D9%85-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA-20190624/']

    rules = (
        #Rule(LinkExtractor(allow=r'ar.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^^http:\/\/www.2m.ma.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = TwomItem()
            item['content'] = response.xpath('//*[@id="medium-editor"]/p/text()').extract()  
            with open('tm.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

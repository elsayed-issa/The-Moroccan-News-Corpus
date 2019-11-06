# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NadorcityItem
from scrapy.loader import ItemLoader


class NadorCrawlerSpider(CrawlSpider):
    name = 'nador_crawler'
    allowed_domains = ['www.nadorcity.com']
    start_urls = ['https://www.nadorcity.com/%D8%B1%D9%85%D8%B3%D9%8A%D8%B3-%D8%A8%D9%88%D9%84%D8%B9%D9%8A%D9%88%D9%86-%D9%8A%D9%83%D8%AA%D8%A8-%D8%B5%D9%8A%D9%81-%D8%A7%D9%84%D9%86%D8%A7%D8%B8%D9%88%D8%B1-%D8%A8%D9%86%D9%83%D9%87%D8%A9-%D8%A7%D9%84%D8%A3%D8%B2%D8%A8%D8%A7%D9%84-%D9%88%D9%84%D8%B3%D8%B9%D8%A9-%D8%A7%D9%84%D9%86%D8%A7%D9%85%D9%88%D8%B3_a77378.html']

    rules = (
        #Rule(LinkExtractor(allow=r'topics.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^^https:\/\/www.nadorcity.com.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = NadorcityItem() 
            item['content'] = response.xpath('//*[@class="access firstletter"]/div/text()').extract() 
            with open('nador.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

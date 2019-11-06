# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AkhbaronaItem
from scrapy.loader import ItemLoader


class GoodCrawlerSpider(CrawlSpider):
    name = 'akhbar_crawler'
    allowed_domains = ['www.akhbarona.com']
    start_urls = ['https://www.akhbarona.com/economy/index.1.html',
                  'https://www.akhbarona.com/politic/index.1.html',
                  'https://www.akhbarona.com/national/index.1.html',
                  'https://www.akhbarona.com/sport/index.1.html',
                  'https://www.akhbarona.com/world/index.1.html',
                  'https://www.akhbarona.com/health/index.1.html',
                  'https://www.akhbarona.com/technology/index.1.html',
                  'https://www.akhbarona.com/culture/index.1.html',
                  'https://www.akhbarona.com/last/index.1.html']

    rules = (
        Rule(LinkExtractor(allow=r'(economy|politic|national|sport|world|health|technology|culture|last).*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = AkhbaronaItem()
            item['content'] = response.xpath('//*[@id="article_body"]/p/text()').extract() 
            with open('akhbar.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

        

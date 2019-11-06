# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BarlamaneItem
from scrapy.loader import ItemLoader


class BarCrawlerSpider(CrawlSpider):
    name = 'bar_crawler'
    allowed_domains = ['www.barlamane.com']
    start_urls = ['https://www.barlamane.com/%d9%85%d8%b9%d8%a7%d8%b1%d8%b6%d9%88-%d8%a8%d9%86%d8%b4%d9%85%d8%a7%d8%b4-%d9%8a%d8%ad%d8%af%d8%af%d9%88%d9%86-%d8%aa%d8%a7%d8%b1%d9%8a%d8%ae-%d8%a7%d9%84%d9%85%d8%a4%d8%aa%d9%85%d8%b1-%d8%a7%d9%84/']

    rules = (
        #Rule(LinkExtractor(allow=r'category.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^https:\/\/www.barlamane.com.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = BarlamaneItem()
        item['content'] = response.xpath('//*[@class="content"]/p/text()').extract()
        with open('bar.txt','a') as f:
            f.write('content: {0}\n'.format(item['content']))
        yield item

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MorctelegraphItem
from scrapy.loader import ItemLoader


class GoodCrawlerSpider(CrawlSpider):
    name = 'telegraph_crawler'
    allowed_domains = ['maroctelegraph.com']
    start_urls = ['https://maroctelegraph.com/2019/06/%d9%85%d9%86-%d9%85%d9%88%d9%82%d8%b9-%d8%a7%d9%84%d9%85%d8%b9%d8%a7%d8%b1%d8%b6%d8%a9-%d8%a7%d9%84%d8%a8%d9%8a%d8%ac%d9%8a%d8%af%d9%8a-%d9%8a%d8%b3%d8%aa%d8%ad%d8%b6%d8%b1-%d8%a7%d9%84%d8%aa%d9%82/']

    rules = (
        #Rule(LinkExtractor(allow=r'topics.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^https:\/\/maroctelegraph.com.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = MorctelegraphItem()
            item['content'] = response.xpath('//*[@class="entry-content clearfix"]/p/text()').extract()
            with open('tele.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item


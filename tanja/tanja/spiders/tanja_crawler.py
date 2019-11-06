# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TanjaItem
from scrapy.loader import ItemLoader


class TanjaCrawlerSpider(CrawlSpider):
    name = 'tanja_crawler'
    allowed_domains = ['tanja24.com']
    start_urls = ['https://tanja24.com/%d8%a7%d9%84%d9%85%d8%ba%d8%b1%d8%a8-%d9%8a%d8%b9%d9%84%d9%86-%d9%85%d8%b4%d8%a7%d8%b1%d9%83%d8%aa%d9%87-%d9%81%d9%8a-%d9%85%d8%a4%d8%aa%d9%85%d8%b1-%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%85%d8%a9-%d9%84/']

    rules = (
        #Rule(LinkExtractor(allow=r'topics.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^https:\/\/tanja24.com.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = TanjaItem() 
            item['content'] = response.xpath('//*[@class="entry-content clearfix single-post-content"]/p/text()').extract() 
            with open('tanga.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

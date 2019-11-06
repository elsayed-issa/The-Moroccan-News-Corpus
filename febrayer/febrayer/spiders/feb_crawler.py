# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FebrayerItem
from scrapy.loader import ItemLoader


class FebCrawlerSpider(CrawlSpider):
    name = 'feb_crawler'
    allowed_domains = ['www.febrayer.com']
    start_urls = ['https://www.febrayer.com/644933.html']

    rules = (
        #Rule(LinkExtractor(allow=r'category.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^https:\/\/www.febrayer.com.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = FebrayerItem()
            item['content'] = response.xpath('//*[@class="single-content"]/p/text()').extract()
            with open('feb.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

        #next_page_url = response.xpath('//*[@class="col-md-12"]/a[@class="nav-btn left"]/@href').extract_first()
        #if next_page_url:
            #yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_item)

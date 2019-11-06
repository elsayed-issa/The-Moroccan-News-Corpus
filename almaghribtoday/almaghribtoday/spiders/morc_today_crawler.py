# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AlmaghribtodayItem
from scrapy.loader import ItemLoader


class MorcTodayCrawlerSpider(CrawlSpider):
    name = 'morc_today_crawler'
    allowed_domains = ['www.almaghribtoday.net']
    start_urls = ['https://www.almaghribtoday.net/1187/151638-%D9%83%D9%88%D8%B4%D9%86%D8%B1-%D9%8A%D8%A4%D9%83%D8%AF-%D8%A3%D9%86-%D8%B1%D9%81%D8%B6-%D8%A7%D9%84%D9%81%D9%84%D8%B3%D8%B7%D9%8A%D9%86%D9%8A%D9%8A%D9%86-%D9%84%D8%AE%D8%B7%D8%A9-%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85-%D8%AE%D8%B7%D8%A3-%D8%A7%D8%B3%D8%AA%D8%B1%D8%A7%D8%AA%D9%8A%D8%AC%D9%8A']

    rules = (
        #Rule(LinkExtractor(allow=r'topics.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'[^https:\/\/www.almaghribtoday.net.]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = AlmaghribtodayItem() 
            item['content'] = response.xpath('//*[@id="balmon"]/p/text()').extract() 
            with open('morc_today.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item
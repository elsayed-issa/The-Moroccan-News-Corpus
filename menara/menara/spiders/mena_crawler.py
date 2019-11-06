# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MenaraItem
from scrapy.loader import ItemLoader


class MorcCrawlerSpider(CrawlSpider):
    name = 'mena_crawler'
    allowed_domains = ['www.menara.ma']
    start_urls = ['https://menara.ma/article/categorie/%D8%A5%D9%82%D8%AA%D8%B5%D8%A7%D8%AF',]

    rules = (
        Rule(LinkExtractor(allow=r'categorie.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'article.*'), callback='parse_item', follow=True),
        )

    def parse_item(self, response):
        #articles = response.xpath('//*[@class="entry-content clearfix"]')
        
        #for article in articles:
            item = MenaraItem()
            item['title'] = response.xpath('//h4/a/text()').extract()     
            #item['content'] = response.xpath('//*[@class="p-content"]/div/p/text()').extract()
            yield item

            next_page_url = response.xpath('//li/a[@aria-label="Next"]/@href').extract_first() 
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(response.urljoin(absolute_next_page_url), callback=self.parse_item)
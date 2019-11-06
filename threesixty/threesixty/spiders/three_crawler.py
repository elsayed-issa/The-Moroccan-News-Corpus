# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from ..items import GoodItem
from scrapy.loader import ItemLoader


class GoodCrawlerSpider(CrawlSpider):
    name = 'three_crawler'
    allowed_domains = ['ar.le360.ma']
    start_urls = ['http://ar.le360.ma/politique/150906']

    rules = (
        Rule(LinkExtractor(allow=r'politique.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            #item = GoodItem()
            #item['url'] = article.xpath('a[@class="read-more"]/@href').extract()
            #item['url'] = article.xpath('a[@class="read-more"]/text()').extract()
            #item['title'] = article.xpath('//*[@class="col-md-12"]/h1/text()').extract_first() 
            content = response.xpath('//*[@class="articles-holder"]/div[@class="ctn"]/text()').extract()
            yield {'content':content}

            next_page_url = response.xpath('//*[@class="pager-next last"]/a/@href').extract_first()
            if next_page_url:
                absolute_next_page_url = response.urljoin(next_page_url)
                yield scrapy.Request(absolute_next_page_url, callback=self.parse)

        

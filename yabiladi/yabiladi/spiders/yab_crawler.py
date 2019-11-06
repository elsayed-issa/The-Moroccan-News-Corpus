# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import YabiladiItem
from scrapy.loader import ItemLoader


class YabCrawlerSpider(CrawlSpider):
    name = 'yab_crawler'
    allowed_domains = ['ar.yabiladi.com']
    start_urls = ['https://www.yabiladi.ma/articles/']

    rules = (
        Rule(LinkExtractor(allow=r'articles.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            item = YabiladiItem()
            item['content'] = response.xpath('//*[@itemprop="articleBody"]/p/text()').extract()
            with open('yab.txt','a') as f:
                f.write('content: {0}\n'.format(item['content']))
            yield item

            next_page = response.xpath('//*[@class="page_num"]/@href').extract_first()
            absoulte_next_page = response.urljoin(next_page)
            yield scrapy.Request(absoulte_next_page, callback=self.parse_item)

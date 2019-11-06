# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from ..items import HibapressItem
from scrapy.loader import ItemLoader


class HibaSpider(Spider):
    name = 'hiba_politics'
    allowed_domains = ['ar.hibapress.com']
    start_urls = ['https://ar.hibapress.com/section-3.html']

    def parse(self, response):
        # This is to get all the links to all the 13 menu items
        pages = response.xpath('//*[@class="entry-title"]')
        for page in pages:
            link = page.xpath('.//a/@href').extract_first()
            yield Request(link, callback=self.parse_page)
            
    def parse_page(self, response):
        item = HibapressItem()
        #item['title'] = response.xpath('//h1[@class="post-title entry-title"]/span/text()').extract_first()
        item['content'] = response.xpath('//*[@id="hibapressarticles"]/p/text()').extract()
        with open('log1.txt', 'a') as f:
            f.write('content: {0}\n'.format(item['content']))
        yield item
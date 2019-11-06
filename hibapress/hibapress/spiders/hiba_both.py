# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from ..items import HibapressItem
from scrapy.loader import ItemLoader


class HibaSpider(Spider):
    name = 'hiba_all'
    allowed_domains = ['ar.hibapress.com']
    start_urls = ['https://ar.hibapress.com/section-3.html',
                  'https://ar.hibapress.com/section-20.html',
                  'https://ar.hibapress.com/section-19.html',
                  'https://ar.hibapress.com/section-8.html',
                  'https://ar.hibapress.com/section-24.html',
                  'https://ar.hibapress.com/section-22.html',
                  'https://ar.hibapress.com/section-10.html',
                  'https://ar.hibapress.com/section-2.html',
                  'https://ar.hibapress.com/section-9.html',
                  'https://ar.hibapress.com/section-99.html',
                  'https://ar.hibapress.com/section-6.html']

    def parse(self, response):
        # This is to get all the links to all the 13 menu items
        pages = response.xpath('//*[@class="entry-title"]')
        for page in pages:
            link = page.xpath('.//a/@href').extract_first()
            yield Request(link, callback=self.parse_page)
            
    def parse_page(self, response):
        item = HibapressItem()
        #item['title'] = response.xpath('//h1[@class="post-title entry-title"]/span/text()').extract_first()
        item['body'] = response.xpath('//*[@id="hibapressarticles"]/p/text()').extract()
        yield item




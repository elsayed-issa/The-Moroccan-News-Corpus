# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class HibaSpider(Spider):
    name = 'hiba_economy'
    allowed_domains = ['ar.hibapress.com']
    start_urls = ['https://ar.hibapress.com/section-20.html']

    def parse(self, response):
        # This is to get all the links to all the 13 menu items
        pages = response.xpath('//*[@class="entry-title"]')
        for page in pages:
            link = page.xpath('.//a/@href').extract_first()
            yield Request(link, callback=self.parse_page)
            
    def parse_page(self, response):
        #link = response.meta['link']
        #title = response.xpath('//h1[@class="post-title entry-title"]/span/text()').extract_first()
       body = response.xpath('//*[@id="hibapressarticles"]/p/text()').extract()
       yield{'body': body}
        
       next_page = response.xpath('//*[@class="bdaia-pagination"]/a/@href').extract()
       absolute_next_page = response.urljoin(next_page)
       yield Request(absolute_next_page, callback=self.parse_page)




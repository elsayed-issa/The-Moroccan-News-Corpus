# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class ThreeSpider(Spider):
    name = 'three'
    allowed_domains = ['ar.le360.ma']
    start_urls = ['http://ar.le360.ma/','http://ar.le360.ma/economie/150885']

    def parse(self, response):
        content = response.xpath('//*[@class="articles-holder"]/div[@class="ctn"]/text()').extract() 

        yield{
            "content" : content
        }

        next_page_url = response.xpath('//*[@class="pager-next last"]/a/@href').extract_first()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield Request(absolute_next_page_url, callback=self.parse)


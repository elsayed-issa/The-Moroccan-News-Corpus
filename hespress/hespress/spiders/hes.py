# -*- coding: utf-8 -*-
import scrapy


class HesSpider(scrapy.Spider):
    name = 'hes'
    allowed_domains = ['www.hespress.com']
    start_urls = ['https://www.hespress.com/politique/index.1.html','https://hespress.com/politique/436105.html']

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        content = response.xpath('//*[@id="article_body"]/p/text()').extract()
        yield{'content' : content}

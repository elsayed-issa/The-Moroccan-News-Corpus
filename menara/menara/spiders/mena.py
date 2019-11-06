# -*- coding: utf-8 -*-
import scrapy


class MenaSpider(scrapy.Spider):
    name = 'mena'
    allowed_domains = ['www.menara.ma']
    start_urls = ['https://www.menara.ma/article/categorie/%D9%85%D8%B1%D8%A3%D8%A9']

    def parse(self, response):
        title = response.xpath('//h4/a/text()').extract()
        yield{'title':title}

    def parse_article(self, response):
        pass # see the subjects code

        next_page_url = response.xpath('//*[@aria-label="Next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url,callback=self.parse)

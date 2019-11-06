# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class MorcSpider(Spider):
    name = 'morc'
    allowed_domains = ['www.almaghreb24.com']
    start_urls = ['https://almaghreb24.com/']


    def __init__(self, subject=None):
        self.subject = subject


    def parse(self, response):
        if self.subject:
            subject_url = response.xpath('//*[contains(@title "' + self.subject + '")]/@href').extract_first()
            yield Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            self.logger.info('Scapping all subjects.')
            subjects = response.xpath('//*[@id="menu-menu-principal"]/li/a/@href').extract()
            for subject in subjects:
                yield Request(response.urljoin(subject), callback=self.parse_subject)

    def parse_subject(self, response):
        articles = response.xpath('//*[@itemtype="http://schema.org/Article"]/h2[@class="cat-list-title"]/a/@href')
        for article in articles:
            article_title = article.xpath('.//@h1/text()').extract_first()

            yield{
                'article_title' : article_title
            }



        #pages = response.xpath('//*[@id="menu-menu-principal"]/li/a')
        #for page in pages:
            #link = page.xpath('.//@href').extract_first()

            #yield Request(link, callback=self.parse_page)

    #def parse_page(self, response):
        #link = response.meta['link']

        #title = response.xpath('//*[@itemtype="http://schema.org/Article"]/h2[@class="cat-list-title"]/a/text()').extract()

        #yield{'title': title}

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from ..items import GoodItem
from scrapy.loader import ItemLoader


class GoodCrawlerSpider(CrawlSpider):
    name = 'hes_crawler'
    allowed_domains = ['www.hespress.com']
    start_urls = ['https://www.hespress.com/politique/index.1.html',                
                  'https://www.hespress.com/societe/index.1.html',
                  'https://www.hespress.com/regions/index.1.html',
                  'https://www.hespress.com/economie/index.1.html',
                  'https://www.hespress.com/marocains-du-monde/index.1.html',
                  'https://www.hespress.com/medias/index.1.html',
                  'https://www.hespress.com/faits-divers/index.1.html',
                  'https://www.hespress.com/art-et-culture/index.1.html',
                  'https://www.hespress.com/tamazight/index.1.html',
                  'https://www.hespress.com/orbites/index.1.html',
                  'https://www.hespress.com/sport/index.1.html']

    rules = (
        Rule(LinkExtractor(allow=r'(politique|societe|regions|economie|marocains-du-monde|medias|faits-divers|art-et-culture|tamazight|orbites|sport).*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'[^https:\/\/www.goud.ma]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            #item = GoodItem()
            #item['url'] = article.xpath('a[@class="read-more"]/@href').extract()
            #item['url'] = article.xpath('a[@class="read-more"]/text()').extract()
            #item['title'] = article.xpath('//*[@class="col-md-12"]/h1/text()').extract_first() 
            content = response.xpath('//*[@id="article_body"]/p/text()').extract()
            yield {'content':content}

        

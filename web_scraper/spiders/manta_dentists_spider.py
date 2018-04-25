# -*- coding: utf-8 -*-
import scrapy


class MantaDentistsSpiderSpider(scrapy.Spider):
    name = 'manta_dentists_spider'

    allowed_domains = ['manta.com']
    start_urls = ['https://www.manta.com/search?search_source=nav&search=dentist&search_location=Los+Angeles+CA&pt=34.0396%2C-118.2661']

    def parse(self, response):
        for dentist in response.css('li.list-group-item'):
            yield {
                'title' : dentist.css('strong').extract_first(),
            }

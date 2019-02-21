# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = "redditbot"
    allowed_domains = ["https://scholar.google.com.au/citations?user=zD0vtfwAAAAJ&hl=en"]
    start_urls = (
        'http://www.https://scholar.google.com.au/citations?user=zD0vtfwAAAAJ&hl=en/',
    )

    def parse(self, response):
        pass

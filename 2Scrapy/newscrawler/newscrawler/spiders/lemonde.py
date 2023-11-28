# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ArticleItem


class LemondeSpider(scrapy.Spider):
    name = "lemondev4"
    allowed_domains = ["www.lemonde.fr"]
    start_urls = ['https://www.lemonde.fr']

    def parse(self, response):
        title = response.css('title::text').extract_first()
        all_links = ['https://www.lemonde.fr']
        # print(response.body)
        for link in all_links:
            yield Request(link, callback=self.parse_category)

    def parse_category(self, response):
        for article in response.css(".area--runner").css(".article"):
            print(article)
            title = self.clean_spaces(article.css(".article__title::text").extract_first())
            print(article.css(".article__title"))
            image = article.css("img::attr(data-src)").extract_first()
            description = article.css(".txt3::text").extract_first()

            yield ArticleItem(
                title=title,
                image=image,
                description=description
            )

    def clean_spaces(self, string):
        if string:
            return " ".join(string.split())

import scrapy


class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill", ]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()
            # remove the U+201C and U+201D unicode characters
            text_value = text_value.replace(u'\u201C', '').replace(u'\u201D', '')
            yield {'text': text_value,
                   'author': 'Winston Churchill'}

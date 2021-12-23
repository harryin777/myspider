import scrapy
from scrapy.linkextractors import LinkExtractor


class YAHOO(scrapy.Spider):
    name = "yahoo"

    def start_requests(self):
        urls = [
            'https://finance.yahoo.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        filename = 'finance.yahoo.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        for a in response.css('a'):
            urlText = a.css('::text').extract()
            if 'lucid' in urlText:
                self.log("urlText %s" % urlText)
                self.log("url1111 %s" % a.css('::attr(href)').extract())

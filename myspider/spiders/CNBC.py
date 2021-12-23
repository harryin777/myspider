import scrapy
from scrapy.linkextractors import LinkExtractor


class CNBC(scrapy.Spider):
    name = "cnbc"

    def start_requests(self):
        urls = [
            'https://www.cnbc.com/world/?region=world',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        for a in response.css('a'):
            urlText = a.css('::text').extract()
            self.log("urlText %s \n" % urlText)
            if 'Chinese' in urlText:
                self.log("urlText %s" % urlText)
                self.log("url1111 %s" % a.css('::attr(href)').extract())
        self.log("finish !!!!")

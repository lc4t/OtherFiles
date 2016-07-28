import scrapy
from scrapy.http import Request
from uestc.items import UestcItem
class UestcSpider(scrapy.spiders.Spider):
    name = 'uestc'
    allowed_domains = ['uestc.edu.cn']
    start_urls = [
        'http://www.uestc.edu.cn/'
    ]

    def parse(self, response):

        # sub domain
        for sel in response.selector.re('https?://[A-Za-z0-9_\-\.]*?' + 'uestc.edu.cn' + '/'):  # domain
            item = UestcItem()
            item['url'] = sel
            item['method'] = 'GET'
            item['form_params'] = ''
            item['desc'] = 'sub domain'
            item['referer'] = response.url
            yield item
            yield Request(item['url'], callback=self.parse)

        # sub dir
        for sel in response.selector.re(response.url + '/?[a-zA-Z0-9_\-%]+/?'): # sub dir
            item = UestcItem()
            item['url'] = sel
            item['method'] = 'GET'
            item['form_params'] = ''
            item['desc'] = 'sub dir'
            item['referer'] = response.url
            yield item
            yield Request(item['url'], callback=self.parse)

        # form
        for form in response.selector.xpath('//form'):
            item = UestcItem()
            item['url'] = response.url + form.xpath('@action').extract()[0]
            item['method'] = form.xpath('@method').extract()[0].upper()
            item['form_params'] = '=x&'.join([key.extract()[0] for key in form.xpath('//input/@name')])+'=x'
            item['desc'] = 'form'
            item['referer'] = response.url
            yield item
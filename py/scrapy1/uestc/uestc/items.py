# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UestcItem(scrapy.Item):
    # all str
    url = scrapy.Field()
    method = scrapy.Field()
    form_params = scrapy.Field()
    desc = scrapy.Field()
    referer = scrapy.Field()



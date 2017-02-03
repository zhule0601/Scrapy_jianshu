# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyJianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    autor = scrapy.Field()
    url = scrapy.Field()
    read_num = scrapy.Field()
    like_num = scrapy.Field()
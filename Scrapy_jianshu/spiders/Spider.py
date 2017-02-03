# -*- coding:utf-8 -*-
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from Scrapy_jianshu.items import ScrapyJianshuItem
import urllib

class JianshuSpider(CrawlSpider):
    name = 'spider'
    start_urls = ['http://www.jianshu.com/trending/monthly']
    url = 'http://www.jianshu.com'

    def parse(self, response):
        item = ScrapyJianshuItem()
        selector = Selector(response)

        articles = selector.xpath("//ul/[@class = 'note-list']/li")

        for article in articles:
            title = articles.xpath('//div[@class = "content"]/a[@class="title"]/text()').extract()
            part_url = articles.xpath('//div[@class = "content"]/a/@href').extract()
            author = articles.xpath('//div[@class = "content"]/div[@class="name"]/a/text()').extract()
            read_num = articles.xpath('//div[@class = "content"]/div[@class="meta"]/a/text()').extract()[0]
            like_num = articles.xpath('//div[@class = "content"]/div[@class="meta"]/a/text()').extract()[1]

            item['title'] = title
            item['url'] = 'http://www.jianshu.com' + part_url[0]
            item['author'] = author
            item['read_num'] = read_num
            item['like_num'] = like_num
            yield item




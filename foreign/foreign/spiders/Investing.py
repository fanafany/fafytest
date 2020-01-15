# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
import requests
import json
from scrapy import Selector
from scrapy import Request
from scrapy.loader import ItemLoader
from foreign.items import ForeignItem

class InvestingSpider(scrapy.Spider):
    name = 'Investing'
    allowed_domains = ['cn.investing.com']
    start_urls = 'http://cn.investing.com/news/forex-news/'

    def start_requests(self):
        for i in range(1,2):
            url = self.start_urls + str(i)
            yield Request(url, self.parse)
        yield Request('http://cn.investing.com/news/forex-news/',self.parse)

    def parse(self, response):


        # sel = Selector(text=response.text)
        # url = sel.css(".textDiv a::attr(href)").extract()

        # title = response.xpath("//div[@class='textDiv']/a/text()").extract()
        url = response.css(".textDiv a::attr(href)").extract()
        post_nodes = response.css('.largeTitle article')
        for post_node in post_nodes:
            imgurl = post_node.css('a img::attr(src)').extract_first("")
            post_url = post_node.css('a::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":imgurl}, callback=self.parse_detail)

        #提取下一页并交给scrapy进行下载
        # next_url = response.xpath('//div[@id="paginationWrap"]/div[3]/a/text()').extract_first("")
        # if next_url == "下一页":
        #     next_url = response.xpath('//div[@id="paginationWrap"]/div[3]/a/@href').extract_first("")
        #     yield Request(url=parse.urljoin(response.url, next_url),callback=self.parse)

        # next_url = response.xpath('//a[contains(text(),"下一页")]/@href').extract_first("")
        # yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self,response):

        article_item = ForeignItem()

        urls = response.css(".textDiv a::attr(href)").extract()
        title = response.css("#leftColumn h1::text").extract()
        release_time = response.css(".contentSectionDetails span::text").extract()
        types = response.css(".contentSectionDetails a::text").extract()
        texts = response.css(".WYSIWYG.articlePage p::text").extract()
        text = ''.join(texts)



        article_item["title"] = title
        article_item["release_time"] = release_time
        article_item["types"] = types
        article_item["text"] = text
        # print(article_item)
        print(type(article_item))

        yield article_item




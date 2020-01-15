# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ForeignItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    release_time = scrapy.Field()
    types = scrapy.Field()
    text = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into investing VALUES (%s ,%s, %s, %s)
        """

        params = (self['title'],self["release_time"],self["types"],self["text"])

        return insert_sql, params




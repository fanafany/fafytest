# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-14 14:36 '

import requests
from lxml import etree

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

url = "https://blog.csdn.net/samxx8/article/details/7219433"
req = requests.get(url,headers = header).text
html = etree.HTML(req)
title = html.xpath("//div[@class = 'article-title-box']/h1/text()")
datime = html.xpath("//div[@class='article-bar-top']/span[2]/text()")
titles = ''.join(title)
datimes = ''.join(datime).replace('','')
print(titles)
print(datimes)
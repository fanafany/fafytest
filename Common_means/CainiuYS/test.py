# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-27 13:45 '
import requests
from lxml import etree
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
dics = []
url = 'https://www.cnys.com/article/list_2_1.html'
resp = requests.get(url,header).text
html = etree.HTML(resp)
title = html.xpath("//div[@class='leftLists']/a/@title")
urls = html.xpath("//div[@class='leftLists']/a/@href")
subtitle = html.xpath("//div[@class='nationalListText']/p[1]/text()")
keyword = html.xpath("//div[@class='nationalListText']/p[2]/span/text()")
datime = html.xpath("//div[@class='nationalListTextTig']/span/text()")
for item,titles,subtitles,keywords,datimes in zip(urls,title,subtitle,keyword,keyword):
    url_home = 'https://www.cnys.com/' + item
    req = requests.get(url_home,header).text
    htmls = etree.HTML(req)
    content = htmls.xpath("//div[@class='reads']/p/text()")

    contents = ''.join(content)+'\n'
    print(contents)
    # dic = {
    #     'keywords': keywords,
    #     'title':titles,
    #     'original_link':url_home,
    #     'time':datimes,
    #     'subtitle': subtitles,
    #     'content': contents
    # }
    # dics.append(dic)



# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-27 13:42 '

import requests
from lxml import etree
import json
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor
import datetime
start = datetime.datetime.now()
queue_list = Queue()

def index_spider(url):
    dics = []
    print("当前",url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    resp = requests.get(url, header).text
    html = etree.HTML(resp)
    title = html.xpath("//div[@class='leftLists']/a/@title")
    urls = html.xpath("//div[@class='leftLists']/a/@href")
    subtitle = html.xpath("//div[@class='nationalListText']/p[1]/text()")
    keyword = html.xpath("//div[@class='nationalListText']/p[2]/span/text()")
    datime = html.xpath("//div[@class='nationalListTextTig']/span/text()")
    for item, titles, subtitles, keywords, datimes in zip(urls, title, subtitle, keyword, datime):
        url_home = 'https://www.cnys.com/' + item
        req = requests.get(url_home, header).text
        htmls = etree.HTML(req)
        content = htmls.xpath("//div[@class='reads']/p/text()")
        contents = ''.join(content)
        dic = {
            'keywords': keywords,
            'title': titles,
            'original_link': url_home,
            'time': datimes,
            'subtitle': subtitles,
            'content': contents
        }
        dics.append(dic)
    with open('彩牛养生.json','a',encoding='utf-8')as file:
        file.write(json.dumps(dics,indent=2, ensure_ascii=False))
    end = datetime.datetime.now()
    ens = end - start
    print("共耗时", ens)
if __name__ == '__main__':
    url_home = [
        ['https://www.cnys.com/article/list_1_%d.html' % i for i in range(1,853)],
        ['https://www.cnys.com/article/list_2_%d.html' % i for i in range(1,540)],
        ['https://www.cnys.com/article/list_4_%d.html' % i for i in range(1,116)],
        ['https://www.cnys.com/article/list_5_%d.html' % i for i in range(1,15)],
        ['https://www.cnys.com/article/list_7_%d.html' % i for i in range(1,531)],
        ['https://www.cnys.com/article/list_33_%d.html' % i for i in range(1,205)],
        ['https://www.cnys.com/article/list_28_%d.html' % i for i in range(1,232)],
        ['https://www.cnys.com/article/list_23_%d.html' % i for i in range(1,389)],
        ['https://www.cnys.com/article/list_18_%d.html' % i for i in range(1,160)],
        ['https://www.cnys.com/article/list_13_%d.html' % i for i in range(1,129)],
        ['https://www.cnys.com/article/list_42_%d.html' % i for i in range(1,181)]
    ]
    for s in url_home:
        for i in s:
            queue_list.put(i)
        pool = ThreadPoolExecutor(max_workers=50)
        while queue_list.qsize() > 0:
            pool.submit(index_spider, queue_list.get())



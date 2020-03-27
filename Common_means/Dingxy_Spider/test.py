# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-27 15:48 '
import requests
from lxml import etree
import json
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor

queue_list = Queue()
def index_spider(url):
    dics = []
    print('当前',url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    req = requests.get(url,header).text
    html = etree.HTML(req)
    datime = html.xpath("//dl[@class='x_box12']/dd/p/span/text()")
    title = html.xpath("//dl[@class='x_box12']/dd/p/a/@title")
    urls = html.xpath("//dl[@class='x_box12']/dd/p/a/@href")
    subtitle = html.xpath("//dl[@class='x_box12']/dd/p[2]/text()")
    for item,titles,subtitles,datimes in zip(urls,title,subtitle,datime):
        resp = requests.get(item,header).text
        htmls = etree.HTML(resp)
        content = htmls.xpath("//div[@id='content']/p/text()")
        contents = ''.join(content)
        dic = {
            'title': titles,
            'original_link': item,
            'time': datimes,
            'subtitle': subtitles,
            'content': contents
        }
        dics.append(dic)
    with open('丁香园.json','a',encoding='utf-8')as file:
        file.write(json.dumps(dics,indent=2, ensure_ascii=False))

if __name__ == '__main__':
    url_Home = [
        'http://heart.dxy.cn/tag/news/p-%d' %i for i in range(2,101)
    ]
    for i in url_Home:
        queue_list.put(i)
    pool = ThreadPoolExecutor(max_workers=10)
    while queue_list.qsize() > 0:
        pool.submit(index_spider, queue_list.get())


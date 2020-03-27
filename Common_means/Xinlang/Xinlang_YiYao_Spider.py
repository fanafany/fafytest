# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-27 12:37 '
import requests
from lxml import etree
import json
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor
import datetime
start = datetime.datetime.now()
queue_list = Queue()
def index_spider(url):
    print("当前",url)
    header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
    resp = requests.get(url,header).text
    html = etree.HTML(resp)
    title = html.xpath("//div[@class='indextext-right']/div/a/text()")
    urls = html.xpath("//div[@class='indextext-right']/div/a/@href")
    datime = html.xpath("//div[@class='indexright-botbox']/span/text()")
    subtitle = html.xpath("//p[@class='indextext-ms']/text()")

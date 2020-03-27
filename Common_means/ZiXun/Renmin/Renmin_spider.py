import requests
from lxml import etree
import asyncio
import aiohttp
import re
import math
import time
import json
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor
#创建队列
queue_list = Queue()
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}
dics = []

def index_home(url_home):
    lis_url = []

    response = requests.get(url=url_home, headers=header)
    response.encoding = 'gb2312'
    if response.status_code == 200:
        html = etree.HTML(response.text)
        url = html.xpath("//div[@class='newsItems']/a/@href")
        keyword = html.xpath('//div[@class="subNav"]/a[3]/text()')
        keywords = ''.join(keyword)
        for item in url:
            urls = 'http://health.people.com.cn/'+item
            lis_url.append(urls)
            lis_url.append(keywords)


    return lis_url

def index_parse(url):
    for item,keywitem in zip(index_home(url)):
        req = requests.get(item,header).text
        htmls = etree.HTML(req)
        title = htmls.xpath("//div[@class='title']/h2/text()")
        titles = ''.join(title)
        content = htmls.xpath("//div[@class='artOri']/text()".replace('来源：', ''))
        conts = ''.join(content).replace("来源：", "")
        contents = htmls.xpath("//div[@class='artDet']/p/text()")
        contems = ''.join(contents)
        sutit = htmls.xpath("//div[@class='artDet']/p[position()>0 and position()<3]/text()")
        subtitle = ''.join(sutit)
        keywords = keywitem
        dic = {

            "title": titles,
            'time': conts,
            'fcount': item,
            'keywords': keywords,
            'subtitle': subtitle,
            'content': contems
        }
        dics.append(dic)
        print(dics)
    with open('data3.json','a',encoding='utf-8')as file:
        file.write(json.dumps(dics,indent=2, ensure_ascii=False))
url_Home = [
    ['http://health.people.com.cn/GB/408572/index%d.html'%i for i in range(1,2)],
    ['http://health.people.com.cn/GB/408575/index%d.html'%i for i in range(1,2)]
       ]

if __name__ == '__main__':
    for i in url_Home:
        for s in i:
            queue_list.put(s)
            pool = ThreadPoolExecutor(max_workers=3)
            while queue_list.qsize()>0:
                pool.submit()
            sou = index_home(s)
            print(sou)
            # gou = index_parse(sou)



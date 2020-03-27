# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-27 10:32 '

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
            'Host':'feed.mix.sina.com.cn',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
    # datas = {
    #     'pageid':'67',
    #     'lid':'566',
    #     'num':'10',
    #     'page':'1',
    #     'callback':'feedCardJsonpCallback',
    #     '_':'1585275166810'
    #
    # }
    dics = []
    response = requests.get(url,headers=header).content
    result=json.loads(response)
    html = result['result']['data']
    for item in html:
        url_cont = item['url']
        print(len(url_cont))
        req = requests.get(url_cont,header)
        req.encoding = 'utf-8'
        htmls = etree.HTML(req.text)
        content = htmls.xpath("//div[@class='article']/p/text()")
        contents = ''.join(content)
        if contents=='':
            cont = htmls.xpath("//div[@class='content_wrappr_left']/div[2]/p/text()")
            contents = ''.join(cont)
        datime = htmls.xpath("//div[@class='date-source']/span[1]/text()")
        datimes = ''.join(datime)
        if datimes == '':
            time = htmls.xpath("//div[@id='page-tools']/span[1]/span[1]/text()")
            datimes = ''.join(time)
        dic = {
            "title":item['title'],
            "subtitle":item['intro'],
            "original_link":item["url"],
            "keywords":item["keywords"],
            "time":datimes,
            "content":contents
        }
        dics.append(dic)
    with open('新浪资讯.json','a',encoding='utf-8')as file:
        file.write(json.dumps(dics,indent=2, ensure_ascii=False))
    end = datetime.datetime.now()
    ens = end - start
    print("共耗时", ens)



if __name__ == '__main__':
    # url = 'http://feed.mix.sina.com.cn/api/roll/get?pageid=67&lid=566&num=10&page=1&callbac'
    url_home = [
        'http://feed.mix.sina.com.cn/api/roll/get?pageid=67&lid=566&num=30&page=%d&callbac' %i for i in range(1,84)
    ]
    for s in url_home:
        queue_list.put(s)
    pool = ThreadPoolExecutor(max_workers=30)
    while queue_list.qsize() > 0:
        pool.submit(index_spider,queue_list.get())

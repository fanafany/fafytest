# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-27 16:49 '
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
    req = requests.get(url,header)
    req.encoding = 'gb2312'
    html = etree.HTML(req.text)

    title = html.xpath("//div[@class='DlistWfc']/h2/a/text()")
    urls = html.xpath("//div[@class='DlistWfc']/h2/a/@href")
    subtitle = html.xpath("//div[@class='DlistWfc']/p[2]/text()")
    keyword = html.xpath("//div[@class='DlistWfc']/div[3]/a[1]/text()")
    for item,titles,subtitles,keywords in zip(urls,title,subtitle,keyword):
        items = 'https:'+item
        resp = requests.get(items,header)
        resp.encoding = 'gb2312'
        htmls = etree.HTML(resp.text)
        content = htmls.xpath("//div[@class='new_cont detail_con']/p/text()")
        contents = ''.join(content)
        if contents == '':
            continue
        datime = htmls.xpath("//div[@class='title_txt']/span[1]/text()")
        datimes = ''.join(datime)
        dic = {
            'title': titles,
            'original_link': items,
            'time': datimes,
            'keywords':keywords,
            'subtitle': subtitles,
            'content': contents
        }
        dics.append(dic)
    with open('99健康1.json','a',encoding='utf-8')as file:
        file.write(json.dumps(dics,indent=2, ensure_ascii=False))

if __name__ == '__main__':
    url_Home = [
        ['https://zyk.99.com.cn/zyys/ysyd/list_1288_%d.html' %i for i in range(1,216)],
        ['https://zyk.99.com.cn/zyys/jjys/list_1291_%d.html' %i for i in range(1,300)],
        ['https://zyk.99.com.cn/zyys/nvys/list_1295_%d.html' %i for i in range(1,317)],
        ['https://zyk.99.com.cn/zyys/nrys/list_1294_%d.html' %i for i in range(1,151)],
        ['https://zyk.99.com.cn/zyys/sjys/list_1298_%d.html' %i for i in range(1,155)],
        ['https://zyk.99.com.cn/changshi/list_2005_%d.html' %i for i in range(1,93)],
        ['https://zyk.99.com.cn/zymr/list_1265_%d.html' %i for i in range(1,173)],
        ['https://zyk.99.com.cn/zyjf/list_1279_%d.html' %i for i in range(1,120)],
        ['https://zyk.99.com.cn/wwwq/list_1308_%d.html' %i for i in range(1,59)],
        ['https://nan.99.com.cn/baojian/578-%d.htm' %i for i in range(1,1205)],
        ['https://nv.99.com.cn/baojian/521-%d.htm' %i for i in range(1,1435)],
        ['https://jf.99.com.cn/ssbd/221-%d.htm' %i for i in range(1,634)],
        ['https://ys.99.com.cn/slys/1997-%d.htm' %i for i in range(1,405)],
        ['https://ys.99.com.cn/jjys/479-%d.htm' %i for i in range(1,215)],
        ['https://ys.99.com.cn/yingyang/478-%d.htm' %i for i in range(1,433)],
        ['https://nk.99.com.cn/hl/3082-%d.htm' %i for i in range(1,67)],
    ]
    for i in url_Home:
        for s in i:
            queue_list.put(s)
        pool = ThreadPoolExecutor(max_workers=30)
        while queue_list.qsize() > 0:
            pool.submit(index_spider, queue_list.get())
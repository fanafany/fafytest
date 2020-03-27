# url = [
#     ['123Pqq%d'%i for i in range(1,5)],
#     ['166666%d'%i for i in range(1,5)]
#        ]
#
# for i in url:
#     for s in i:
#         print(s)
# import requests
# from lxml import etree
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
# }
# url = 'http://health.people.com.cn/n1/2020/0326/c14739-31649002.html'
# resp= requests.get(url = url,headers=header)
# resp.encoding='gb2312'
# html = etree.HTML(resp.text)
# content = html.xpath("//div[@class='artDet']/p[position()>0 and position()<3]/text()")
# contents = ''.join(content)
# print(contents)

import requests
from lxml import etree
import json
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor


queue_list = Queue()
def index_spider(url):
    print('当前',url)
    header = {
        'Host':'health.people.com.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    response = requests.get(url,header)
    response.encoding = "gb2312"
    html = etree.HTML(response.text)
    urls = html.xpath('//div[@class="newsItems"]/a/@href')
    keyword = html.xpath('//div[@class="subNav"]/a[3]/text()')
    keywords = ''.join(keyword)
    dics = []
    s = 0
    lens = len(urls)
    for i in urls:
        item = 'http://health.people.com.cn'+i
        # print(item)
        try:
            res = requests.get(item,header)
            res.encoding = 'gb2312'
            htmls = etree.HTML(res.text)
            title = htmls.xpath("//div[@class='title']/h2/text()")
            titles = ''.join(title)
            content = htmls.xpath("//div[@class='artOri']/text()".replace('来源：',''))
            conts = ''.join(content).replace("来源：","")
            contents = htmls.xpath("//div[@class='artDet']/p/text()")
            contems = ''.join(contents)
            sutit = htmls.xpath("//div[@class='artDet']/p[position()>0 and position()<3]/text()")
            subtitle = ''.join(sutit)
            s += 1
            dic = {

                "title":titles,
                'time':conts,
                'original_link':item,
                'keywords':keywords,
                'subtitle':subtitle,
                'content':contems
            }
            dics.append(dic)
        except:
            pass
    with open('人民网.json','a',encoding='utf-8')as file:
        file.write(json.dumps(dics,indent=2, ensure_ascii=False))
    # print('正在输出第',n)
    sou = lens + lens
    print(sou)
    return dics

if __name__ == '__main__':
    # print(dic)
    url_Home = [
        ['http://health.people.com.cn/GB/408572/index%d.html' % i for i in range(1, 14)],
        ['http://health.people.com.cn/GB/408575/index%d.html' % i for i in range(1, 14)],
        ['http://health.people.com.cn/GB/408571/index%d.html' % i for i in range(1, 14)]
    ]
    for i in url_Home:
        for s in i:
            queue_list.put(s)
        pool = ThreadPoolExecutor(max_workers=10)
        while queue_list.qsize()> 0:
            pool.submit(index_spider,queue_list.get())
        # print(text)
        # print('-------------------------------------')
        # print('-------------------------------------')

# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-30 9:02 '
import requests
from lxml import etree
from time import sleep
from selenium import webdriver
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor

session = requests.Session()
queue_list = Queue()
def index_spider(url):
    dec = []
    browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe")
    # url = 'http://xueshu.baidu.com/s?wd=Scaling%20games%20to%20epic%20proportion.'
    header = {
        'Host':'xueshu.baidu.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    cookie = {
        'Cookie':'BAIDUID=85C4F78B6E002EFA95EBA2FBAD7E5F00:FG=1; BDUSS=jJxVmYzVXNCaDZ2aVFEZ1hXRW94cDk4S2tuUlhrZGw1VzBiOHVyTW5wbn44UHBkRVFBQUFBJCQAAAAAAAAAAAEAAABNoh9WemZzeTUyMDIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP9j013~Y9Ndc; BIDUPSID=6EBA735E88065BC4A58B96B50F73D38F; jshunter-uuid=24c095a9-4821-4595-b3a0-6d3fb2aff161; PSTM=1585530223; BDRCVFR[w2jhEs_Zudc]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSVRTM=217; H_PS_PSSID='
    }
    req = requests.get(url,header).text
    html = etree.HTML(req)
    href = html.xpath("//div[@class='row journal_conf_list']/div/ul/li[4]/span[2]/a/@href")
    return href


if __name__ == '__main__':
    index_Home = [
        ['https://www.datalearner.com/conference/sigmod/60001274'],
        ['https://www.datalearner.com/conference/sigmod/60001272'],
        ['https://www.datalearner.com/conference/sigmod/60001273'],
        ['https://www.datalearner.com/conference/sigmod/60001270'],
        ['https://www.datalearner.com/conference/sigmod/60001269'],
        ['https://www.datalearner.com/conference/sigmod/60001271'],
    ]
    for i in index_Home:
        for s in i:
            queue_list.put(s)
        pool = ThreadPoolExecutor(max_workers=1)
        while queue_list.qsize() > 0:
            pool.submit(index_spider, queue_list.get())
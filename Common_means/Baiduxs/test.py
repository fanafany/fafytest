# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-30 11:39 '
from selenium import webdriver
import requests
import time
from lxml import etree
from collections import Counter
header = {
    'Host':'xueshu.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
cookie = {
    'Cookie':'BAIDUID=85C4F78B6E002EFA95EBA2FBAD7E5F00:FG=1; BDUSS=jJxVmYzVXNCaDZ2aVFEZ1hXRW94cDk4S2tuUlhrZGw1VzBiOHVyTW5wbn44UHBkRVFBQUFBJCQAAAAAAAAAAAEAAABNoh9WemZzeTUyMDIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP9j013~Y9Ndc; BIDUPSID=6EBA735E88065BC4A58B96B50F73D38F; jshunter-uuid=24c095a9-4821-4595-b3a0-6d3fb2aff161; PSTM=1585530223; BDRCVFR[w2jhEs_Zudc]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSVRTM=217; H_PS_PSSID='
}

f = open("Baiduwd.txt","r")  # 返回一个文件对象
ace = []
key = []
lines = f.readlines()      #读取全部内容 ，并以列表方式返回
for line in lines:
    sou = line.replace('\\n','')
    ace.append(sou)
print(len(ace))
for url in ace:
    req = requests.get(url=url,headers=header)
    html = etree.HTML(req.text)
    keyworld = html.xpath("//p[@class='kw_main']/span/a/text()")
    keyworlds = ','.join(keyworld)
    if keyworlds == '':
        continue
    keyes = keyworlds.split(',')
    print(keyes)
    key.append(keyworlds)


kes = ''.join(key)
kess = kes.split()
c2 = Counter(kess)
print('常用的200个关键词:',c2.most_common(200))


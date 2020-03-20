# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-21 10:06 '
import time, datetime
import json
import requests
import re
from openpyxl import workbook
from openpyxl import load_workbook
import openpyxl
import os
import urllib
from time import sleep
import socket

os.chdir('G:\ChangZhi\大唐集团\SVG')
def parse(tit):
    socket.setdefaulttimeout(60)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '数据'
    sheet['A1'] = '标题'
    sheet['B1'] = '时间'
    global ws
    ls = []
    lt = []
    ld = []
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Host':'tang.cdt-ec.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    for si in range(1,500):
        url = 'http://tang.cdt-ec.com/potal-web/pendingGxnotice/where?publish_time=&publish_times=&purchase_unit=&message_title={}&message_type=0&pageno={}&pagesize=30'.format(tit,si)
        req = requests.get(url,headers=header).text
        if req == '[ ]':
            break
        resq = req.encode('utf-8').decode('utf-8')
        jons = json.loads(resq)
        for i in jons:
            title = i['message_title']
            titles = ''.join(title).replace("\\","").replace("-","").replace('"','').replace('/','')
            if len(titles)>55:
                titles = titles[0:50]
            datime = i['deadline']
            pdf = i['pdf_url']
            da = str(datime)
            res = re.findall('\d{10}', da)
            resp = ''.join(res)
            timeArray = time.localtime(int(resp))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            ls.append([titles, otherStyleTime])

            file = urllib.request.urlopen(pdf)
            with open(str(title) + '.pdf', 'wb')as fp:
                fp.write(file.read())
                sleep(2)
            file.close()

        for row in ls:
            sheet.append(row)
        wb.save(tit+'.xlsx')
        print('正在爬取'+'第'+str(si+1)+'页数据！')




while True:

    parse(str(input("请输入关键字:")))


__author__ = 'fanafany'
__date__ = '2020-03-19 12:02 '
import requests
import time
import pymysql
import xlwt
import datetime
from openpyxl import Workbook
wb = Workbook()
 # 激活 worksheet
ws = wb.active
rs = ['姓名', '电话', '网站Id', '所在地', '网站编号', '客户编号', '进入', '沟通状态']
ws.append(rs)
start = datetime.datetime.now()

def handle_index():
    for i in range(1,76172):
        times = str(int(time.time()))
        url = 'https://api-pangu.songshuai.com/TmkClue/GetTmkPublicPoolList'

        cookie = {
             'cookie':'SERVERID=b1b03b1d4c7d95cc57e6ec58b773045f|{0}|{1};'.format(times,times)
        }
        headers = {
            'Authorization':'Bearer d78d9c88-b83a-4d49-ad91-71d243cc68dc',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
        }
        dates = {
            'PageSize':10,
            'PageIndex':i,
            "Where":'{"Reasonids":[],"PublicPoolId":[],"SeachType":1,"SearchKey":"","ClueStatus":[],"CurrentProvince":"","CurrentCity":"","CurrentDistrct":"","CreateTimeStart":"","CreateTimeEnd":"","LastCommunicateTimeStart":"","LastCommunicateTimeEnd":""}'
        }
        req = requests.post(url,data=dates,cookies=cookie,headers=headers).json()
        total = req['result']['Body']

        for item in total:
            name = item['CustomName']
            mobileid = item['MobileId']
            ProvinceName = item['ProvinceName']
            # CityName = item['CityName']
            LastCommunicateContent = item['LastCommunicateContent']
            CustomNo = item['CustomNo']
            ClueNo = item['ClueNo']
            ClueOwnerName = item['ClueOwnerName']
            urls = 'https://api-pangu.songshuai.com/CustomCenter/GetContactById?id={}'.format(mobileid)
            resp = requests.get(urls,cookies=cookie,headers=headers).json()
            mobile = resp['result']
            gs = name+','+str(mobile)+','+str(mobileid)+','+ProvinceName+','+str(CustomNo)+','+str(ClueNo)+','+ClueOwnerName+','+LastCommunicateContent
            gsh = gs.split(',')
            # print(gsh)
            # print(name+','+str(mobile)+','+str(mobileid)+','+ProvinceName+','+CityName+','+str(CustomNo)+','+str(ClueNo)+','+str(ClueGuid)+','+ClueOwnerName+','+LastCommunicateContent)
            ws.append(gsh)
        print('正在爬取第'+str(i)+'页数据')
        wb.save('盘古数据.xls')
    sj = i * 10
    print('一共' + str(sj) + '数据')
    end = datetime.datetime.now()
    hands = end-start
    print('一共耗时:'+str(hands))




handle_index()
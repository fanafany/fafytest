# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-19 12:02 '
import requests
import time
import pymysql
import xlwt
from openpyxl import workbook
from openpyxl import load_workbook
import openpyxl
def get_conn():
    db = pymysql.connect(host="localhost",port=3306,
                   user="root",password="root",
                   db="article",charset="gbk")
    return db

def insert(cur, sql, args):
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('盘古数据', cell_overwrite_ok=True)
head = ['姓名', '电话', '网站Id', '所在地', '网站编号', '客户编号', '进入', '沟通状态']
for h in range(len(head)):
    sheet.write(0, h, head[h])
def handle_index():

    times = str(int(time.time()))
    url = 'https://api-pangu.songshuai.com/TmkClue/GetTmkPublicPoolList'

    cookie = {
         'cookie':'SERVERID=b1b03b1d4c7d95cc57e6ec58b773045f|{0}|{1};'.format(times,times)
    }
    headers = {
        'Authorization':'Bearer 59e8e4c5-cc36-497e-a122-0e0cd2adecc8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
    }
    dates = {
        'PageSize':10,
        'PageIndex':1,
        "Where":'{"Reasonids":[],"PublicPoolId":[],"SeachType":1,"SearchKey":"","ClueStatus":[],"CurrentProvince":"","CurrentCity":"","CurrentDistrct":"","CreateTimeStart":"","CreateTimeEnd":"","LastCommunicateTimeStart":"","LastCommunicateTimeEnd":""}'
    }
    req = requests.post(url,data=dates,cookies=cookie,headers=headers).json()
    total = req['result']['Body']

    for item in total:
        name = item['CustomName']
        mobileid = item['MobileId']
        ProvinceName = item['ProvinceName']
        CityName = item['CityName']
        LastCommunicateContent = item['LastCommunicateContent']
        CustomNo = item['CustomNo']
        ClueNo = item['ClueNo']
        ClueOwnerName = item['ClueOwnerName']
        urls = 'https://api-pangu.songshuai.com/CustomCenter/GetContactById?id={}'.format(mobileid)
        resp = requests.get(urls,cookies=cookie,headers=headers).json()
        mobile = resp['result']
        gs = name+','+str(mobile)+','+str(mobileid)+','+ProvinceName+CityName+','+str(CustomNo)+','+str(ClueNo)+','+ClueOwnerName+','+LastCommunicateContent
        gsh = gs.split(',')
        print(gsh)
        # print(name+','+str(mobile)+','+str(mobileid)+','+ProvinceName+','+CityName+','+str(CustomNo)+','+str(ClueNo)+','+str(ClueGuid)+','+ClueOwnerName+','+LastCommunicateContent)
        i=1

        for i in range(1,len(gsh)):
            sheet.write(i,i+1,gsh[i])

        book.save('2221.xls')

handle_index()
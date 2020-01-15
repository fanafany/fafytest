# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-09 15:01 '
import requests
import pymysql
from lxml import etree


def get_conn():
    db = pymysql.connect(host="112.125.24.66",port=3306,
                   user="root",password="FANAfany1298..",
                   db="article",charset="gbk")
    return db


def insert(cur, sql, args):
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)


def parse():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'cn.investing.com',
        'Referer':'https://cn.investing.com/news/forex-news/2',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    url ='https://cn.investing.com/news/forex-news/article-1916843'
    req = requests.get(url,headers=header).text
    html = etree.HTML(req)
    title = html.xpath("//section[@id='leftColumn']/h1/text()")
    release = html.xpath("//div[@class='contentSectionDetails']/span/text()")
    types = html.xpath("//div[@class='contentSectionDetails']/a/text()")
    text = html.xpath("//div[@class='WYSIWYG articlePage']/p/text()")
    tit = ''.join(title)
    rel = ''.join(release)
    typ = ''.join(types)
    te = ''.join(text)
    lis = []

    a ='1'
    b = '2'
    c = '3'
    d ='4'
    conn = get_conn()
    cur = conn.cursor()
    sql = 'insert into investing values(%s,%s,%s,%s)'


    lis.append(tit)
    lis.append(rel)
    lis.append(typ)
    lis.append(te)
    print(lis)
    args = lis
    print(args)
    insert(cur,sql=sql,args=args)
    print('111')
    conn.commit()
    cur.close()
    conn.close()

parse()



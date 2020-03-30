# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-30 12:51 '
import requests
from lxml import etree
from time import sleep
from selenium import webdriver
from Baidu_Spider import index_spider
dec = []
browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe")
index_Home = ['https://www.datalearner.com/conference/icde/60000980','https://www.datalearner.com/conference/icde/60000981','https://www.datalearner.com/conference/icde/60000978','https://www.datalearner.com/conference/icde/60000979','https://www.datalearner.com/conference/icde/60000977']
for s in index_Home:
    url = index_spider(s)
    for i in url:
        for s in range(1,2):
            browser.get(i)
            sleep(1)
            browser.get(i)
            sou = browser.current_url
            if len(sou)==114:
                print(sou)
                dec.append(sou)
            else:
                continue
            sleep(1)

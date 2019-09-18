import pymysql
import pyttsx3
import csv
import os
import codecs
import requests
import json
import pyttsx3.drivers
import pyttsx3.drivers.sapi5
from aip import AipSpeech
from datetime import datetime

import speech_recognition as sr
import re
en = pyttsx3.init()

APP_ID = '16650822'
API_KEY = '5DOXosjtN8NxG5wlF0C4wIzm'
SECRET_KEY = 'oCSfGx5iKBLFzpQHoag7AfgKw0jlBnht'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 图
TURING_KEY = "311b0cd44df6401d8c3045518109a959"
URL = "http://openapi.tuling123.com/openapi/api/v2"
HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}


# 录音
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("请说话:")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())

    return  audio

def get_conn():
    db = pymysql.connect(host="118.24.198.20",port=3306,
                   user="root",password="root",
                   db="article",charset="gbk")
    return db


#天气
def jttq():
    import requests
    import re
    from lxml import etree
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'http://www.tianqi4.com/xuzhou/'
    responses = requests.get(url,headers = headers).text
    res = re.compile(r'<p>(.*?)</p>')
    ress = res.findall(responses)
    sj_su = ','.join(ress)
    sj = sj_su[0:10]
    gw = sj_su[144:154]
    dw = sj_su[162:169]
    fx = sj_su[173:187]
    hz = sj + gw + dw + fx
    return hz

#系统时间
def xt_time():
    import datetime
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now_time

#GBPUSD最新数据：（英美）
def GBPUSD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'GBPUSD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#USDCHF最新数据（美瑞）
def USDCHF_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal  WHERE `name`= 'USDCHF'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#EURUSD最新数据（欧美）
def EURUSD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'EURUSD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#USDJPY最新数据（美日）
def USDJPY_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'USDJPY'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#USDCAD最新数据（美加）
def USDCAD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'USDCAD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

# AUDUSD最新数据（澳美）
def AUDUSD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'AUDUSD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#EURGBP最新数据（欧英）
def EURGBP_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'EURGBP'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#EURAUD 最新数据（欧澳）
def EURAUD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'EURAUD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#EURCHF最新数据（欧瑞）
def EURCHF_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'EURCHF'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#EURJPY 最新数据（欧日）
def EURJPY_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'EURJPY'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#GBPCHF最新数据（英瑞）
def GBPCHF_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'GBPCHF'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#CADJPY 最新数据（加日）
def CADJPY_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'CADJPY'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#GBPJPY 最新数据（英日）
def GBPJPY_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'GBPJPY'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#AUDNZD 最新数据（澳新）：
def AUDNZD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'AUDNZD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#AUDCAD 最新数据（澳加）
def AUDCAD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'AUDCAD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#AUDCHF 最新数据（澳瑞）
def AUDCHF_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'AUDCHF'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#AUDJPY 最新数据（澳日）
def AUDJPY_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'AUDJPY'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#CHFJPY 最新数据（瑞日）
def CHFJPY_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'CHFJPY'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#EURNZD 最新数据（欧新）
def EURNZD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'EURNZD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#EURCAD 最新数据（欧加）
def EURCAD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'EURCAD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#CADCHF最新数据（加瑞）
def CADCHF_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'CADCHF'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#NZDJPY 最新数据（新日）
def NZDJPY_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'NZDJPY'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()

#NZDUSD 最新数据（新美）
def NZDUSD_data():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name,MAX(datime),text from singal WHERE `name`= 'NZDUSD'")
    for i in cur:
        li = ','.join('%s' % times for times in i)

    return li

    cur.close()
    conn.close()




def check_mis(i):  # result  err_on的返回值  有错误退出防止程序错误
    if i == 3301:
        # QMessageBox.about(self, '  ',"音频质量过差")
        # print("音频质量过差")
        return 1
    if i == 3300:
        # QMessageBox.about(self, '  ',"输入参数不正确")
        # print("输入参数不正确")
        return 1
    if i == 3302:
        #  QMessageBox.about(self, '  ',"鉴权失败")
        # print("鉴权失败")
        return 1
    if i == 3308:
        # QMessageBox.about(self, '  ',"音频过长")
        # print("音频过长")
        return 1
    if i == 3309:
        # QMessageBox.about(self, '  ',"音频数据问题")
        # print("音频数据问题")
        return 1
    if i == 3310:
        # QMessageBox.about(self, '  ',"输入的音频文件过大")
        # print("输入的音频文件过大")
        return 1
    if i == 3311:
        # QMessageBox.about(self, '  ',"采样率rate参数不在选项里")
        # print("采样率rate参数不在选项里")
        return 1
    if i == 3312:
        # QMessageBox.about(self, '  ',"音频格式format参数不在选项里")
        # print("音频格式format参数不在选项里")
        return 1


# 播放
def listen():

    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1536,
    })
    i = result['err_no']

    j = check_mis(i)
    if j == 1:
        return 1

    result_text = result["result"][0]

    print("问:" + result_text)

    if '工作' in result_text:

        if '名字' in result_text:
            rate = en.getProperty('rate')
            # en.setProperty('rate', rate - 90)
            text = '帅哥'
            en.say(text)
            print('答',text)
            en.runAndWait()
        elif '时间'and '几点' in result_text:
            text = xt_time()
            en.say('现在是')
            en.say(text)
            print('答',text)
            en.runAndWait()
        elif '品种' in result_text:
            text = '常见的外汇货币对，例如美元、欧元、日元、英镑、加元、澳元、纽元、瑞郎等等'
            en.say(text)
            print('答',text)
            en.runAndWait()
        elif '多大' in result_text:
            text = '十八'
            en.say(text)
            print('答',text)
            en.runAndWait()
        elif '天气' in result_text:
            text = jttq()
            en.say(jttq())
            print(text)
            en.runAndWait()
        elif '江苏盖尔德' in result_text:
            text = '盖尔德是一家专业从事金融市场软件开发的高新科技企业, 为全球超过30个国家和地区提供网络平台服务 !' \
                   '盖尔德致力于向全球个人及机构客户提供安全、稳定、便捷的在线外汇交易服务。' \
                   '盖尔德凭借丰富的交易品种、极具竞争力的点差、透明化的报价及优质的交易执行，以保持在行业内的领先地位。' \
                   '投资者可以在盖尔德享受来自全球外汇市场领导者的优质交易服务。'
            en.say(text)
            print('答',text)
            en.runAndWait()
        elif '最新'in result_text:
            text = read_conn().replace('USDCHF','美瑞').replace('GBPUSD','英美').replace('EURUSD','欧美').replace('USDJPY','美日')\
                .replace('USDCAD','美加').replace('AUDUSD','澳美').replace('EURGBP','欧英').replace('EURAUD','欧澳').replace('EURCHF','欧瑞')\
                .replace('EURJPY','欧日').replace('GBPCHF','英瑞').replace('CADJPY','加日').replace('GBPJPY','英日').replace('AUDNZD','澳新')\
                .replace('AUDCAD','澳加').replace('AUDCHF','澳瑞').replace('AUDJPY','澳日').replace('CHFJPY','瑞日').replace('EURNZD','欧新')\
                .replace('EURCAD','欧加').replace('CADCHF','加瑞').replace('NZDJPY','新日').replace('NZDUSD','新美')
            en.say("最新一条数据是：")
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答',text)
            en.runAndWait()
        elif '英镑和美元' in result_text:
            text = GBPUSD_data().replace('GBPUSD','英美')
            if text[0:6] == 'GBPUSD':
                text = '英美' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答：',text)
            en.runAndWait()
        elif '美元和瑞士'in result_text:
            text = USDCHF_data().replace('USDCHF','美瑞')
            if text[0:6] == 'USDCHF':
                text = '美瑞' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答:',text)
            en.runAndWait()
        elif '欧元和美元' in result_text:
            text = EURUSD_data().replace('EURUSD','欧美')
            if text[0:6] == 'EURUSD':
                text = '欧美' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答',text)
            en.runAndWait()
        elif '澳元和美元' in result_text:
            text = AUDUSD_data().replace('AUDUSD','澳美')
            if text[0:6] == 'AUDUSD':
                text = '澳美' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答',text)
            en.runAndWait()
        elif '美元和日元'in result_text:
            text = USDJPY_data().replace('USDJPY','美日')
            if text[0:6] == 'USDJPY':
                text = '美日' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答',text)
            en.runAndWait()
        elif '美元和加元' in result_text:
            text = USDCAD_data().replace('USDCAD','美加')
            if text[0:6] == 'USDCAD':
                text = '美加' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答',text)
            en.runAndWait()

        elif '欧元和英镑' in result_text:
            text = EURGBP_data().replace('EURGBP', '欧英')
            if text[0:6] == 'EURGBP':
                text = '欧英' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '欧元和澳元' in result_text:
            text = EURAUD_data().replace('EURAUD', '欧澳')
            if text[0:6] == 'EURAUD':
                text = '欧澳' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '欧元和瑞士' in result_text:
            text = EURCHF_data().replace('EURCHF', '欧瑞')
            if text[0:6] == 'EURCHF':
                text = '欧瑞' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '欧元和日元' in result_text:
            text = EURJPY_data().replace('EURJPY', '欧日')
            if text[0:6] == 'EURJPY':
                text = '欧日' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '英镑和瑞士' in result_text:
            text = GBPCHF_data().replace('GBPCHF', '英瑞')
            if text[0:6] == 'GBPCHF':
                text = '英瑞' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '加元和日元' in result_text:
            text = CADJPY_data().replace('CADJPY', '加日')
            if text[0:6] == 'CADJPY':
                text = '加日' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '英镑和日元' in result_text:
            text = GBPJPY_data().replace('GBPJPY', '英日')
            if text[0:6] == 'GBPJPY':
                text = '英日' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '澳元和新西兰' in result_text:
            text = AUDNZD_data().replace('AUDNZD', '澳新')
            if text[0:6] == 'AUDNZD':
                text = '澳新' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '澳元和加元' in result_text:
            text = AUDCAD_data().replace('AUDCAD', '澳加')
            if text[0:6] == 'AUDCAD':
                text = '澳加' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '澳元和瑞士' in result_text:
            text = AUDCHF_data().replace('AUDCHF', '澳瑞')
            if text[0:6] == 'AUDCHF':
                text = '澳瑞' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '澳元和日元' in result_text:
            text = AUDJPY_data().replace('AUDJPY', '澳日')
            if text[0:6] == 'AUDJPY':
                text = '澳日' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '瑞士和日元' in result_text:
            text = CHFJPY_data().replace('CHFJPY', '瑞日')
            if text[0:6] == 'CHFJPY':
                text = '瑞日' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '欧元和新西兰' in result_text:
            text = EURNZD_data().replace('EURNZD', '欧新')
            if text[0:6] == 'EURNZD':
                text = '欧新' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '欧元和加元' in result_text:
            text = EURNZD_data().replace('EURCAD', '欧加')
            if text[0:6] == 'EURCAD':
                text = '欧加' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '加元和瑞士' in result_text:
            text = CADCHF_data().replace('CADCHF', '加瑞')
            if text[0:6] == 'CADCHF':
                text = '加瑞' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '新西兰和日元' in result_text:
            text = NZDJPY_data().replace('NZDJPY', '新日')
            if text[0:6] == 'NZDJPY':
                text = '新日' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()
        elif '新西兰和美元' in result_text:
            text = NZDUSD_data().replace('NZDUSD', '新美')
            if text[0:6] == 'NZDUSD':
                text = '新美' + text[6:]
            en.say(text)
            if '做空' in text:
                en.say("通过大数据分析建议做空")
            elif '做多' in text:
                en.say("通过大数据分析可做多")
            print('答', text)
            en.runAndWait()

        elif '外汇' and '国际期货' in result_text:
            text = '外汇和国际期货最大的区别就是就是交割日。' \
                   '外汇属于现货产品，没有具体的交割日限制，' \
                   '投资人只要想的话就可以无限期的持有，' \
                   '而国际期货产品则有具体的交割日限制，' \
                   '如果到期还没有平仓的话，就会被强制平仓。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '仓位管理' in result_text:
            text = '简单说一句话：斩断亏损，让盈利奔跑。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '外汇交易' and "风险" in result_text:
            text = '交易之前设好止损位，并且一旦开始操作后就严格执行，' \
                   '当汇价朝着有利于方向走时，假如在做多汇价上升就可以提高止损价，' \
                   '如果在做空时汇价下跌是就可以下调止损位，但是反过来就不能这样做了，' \
                   '不然当初做的止损的就违背初衷了'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '爆仓' in result_text:
            text = '合理控制仓位,进场之前就设置止损,心态控制好，趋势做单'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '长线'in result_text:
            text = '短线一般指3天72小时之内，中线指一周左右的时间，12天以上称之为长线。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '影响'and '多大'in result_text:
            text = '好的数据对于外汇货币影响非常大'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '行情' and '影响' in result_text:
            text = '一些重大的突发事件，会对市场心理形成影响，从而使汇率发生变化，' \
                   '其造成结果的程度，也将对汇率的长期变化产生影响。如911事件使美元在短期内大幅贬值等。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '股票' and '不同之处'in result_text:
            text = '首先交易时间不同，其次交易方式，股票只看升不看跌，外汇双向买卖,看涨也看跌' \
                   '股票是实买实卖交易;外汇是保证金交易方式'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '图形'and '外汇交易' in result_text:
            text = '能够全面透彻地观察到市场的真正变化。' \
                   '我们从K线图中，既可看到股价或大市的趋势，' \
                   '也同时可以了解到每日市况的波动情形。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '技术指标' and '重要' in result_text:
            text = '消息面是做为参考，给你一个指引；技术面是分析，两者同样重要。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '外汇' and '品种' in result_text:
            text = '各个货币的自身属性,各货币对之间的相关性强度,避险情绪和风险情绪'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '外汇交易' and '注意' and '因素' in result_text:
            text = '要注意价格预测指我们预期的未来市场的趋势方向,交易策略，或者说时机抉择，' \
                   '确定具体的入市和出市点'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '仓位'and '控制' in result_text:
            text = '仓位应该是持仓水平吧，是个数量词，应该跟船舱道理差不多，' \
                   '比如船舱总高度30米，装了10米的货，那舱位就是10米，' \
                   '只是计量仓位的单位是手而已，日常生活中比如水库里的水位，' \
                   '商场里某个产品的价位，形容的道理是一样的'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '外汇交易'and '意义' in result_text:
            text = '有些做外汇交易的投资者容易对止损和止盈两个环节产生误解,' \
                   '利弗莫尔名言：优秀的投机家们总是在等待，总是有耐心，' \
                   '等待着市场证实他们的判断。要记住，在市场本身的表现证实你的看法之前，' \
                   '不要完全相信你的判断。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '如何' and '控制' in result_text:
            text = '由于人性天生的弱点，时时不自觉地影响我们的操作，一次大亏，' \
                   '足以输掉前面99次的利润，所以严格遵守止损纪律便成为确保投资者在风险市场中生存的唯一法则。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '美元' and '关联性' in result_text:
            text = '各品种走势有诸多关联性，比如强关联、一致性的品种：黄金指数与黄金、欧元、澳元，' \
                   '从当前市场上看，美元作为市场的核心，其走势可影响多个品种'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '趋势'and '适合' in result_text:
            text = '长短线侧重于持仓时间的划分，趋势、波段更侧重于行情波幅的度量，但中间又加入时间因素，' \
                   '通常把长期点边走势定为趋势行情，把短其单边且连续反向走势定为震荡行情。'
            en.say(text)
            print('答', text)
            en.runAndWait()
        elif '做好' in result_text:
            text = '需要丰富的知识,外汇投资是一种理财行为，它涉及到社会学，经济学，投资学，甚至还有农业知识，' \
                   '矿产知识，金融知识，商品贸易知识等等，同时还要考虑客户的收入状况及未来的经济计划及客户本身的心理状态'
            en.say(text)
            print('答', text)
            en.runAndWait()
    elif '休闲' in result_text:
        robot()

def robot(text=""):
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": ""
            },
            "selfInfo": {
                "location": {
                    "city": "徐州",
                    "street": "泉山区"
                }
            }
        },
        "userInfo": {
            "apiKey": TURING_KEY,
            "userId": "starky"
        }
    }

    data["perception"]["inputText"]["text"] = text
    response = requests.request("post", URL, json=data, headers=HEADERS)
    response_dict = json.loads(response.text)

    result = response_dict["results"][0]["values"]["text"]
    print("the AI said: " + result)
    return result

    import datetime
    gou = []
    dtime = datetime.datetime.now()


    conn = get_conn()
    cur = conn.cursor()
    sql = 'insert into singal_txt values(%s,%s)'
    gou.append(result_text)
    gou.append(dtime)
    args = gou
    # print(args)
    # print('是',args)
    insert(cur, sql=sql, args=args)

    conn.commit()
    cur.close()
    conn.close()



    return result_text

# def read_yuyin():
#     conn = get_conn()
#     cur = conn.cursor()
#     sql = 'insert into singal_txt values(%s)'
#     args = listen()
#     print(args)
#     # print('是',args)
#     insert(cur, sql=sql, args=args)
#
#     conn.commit()
#     cur.close()
#     conn.close()
#     return read_yuyin()






#按照时间排列最新数据
def read_conn():
    ds = []
    dt = []
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT name,datime,text from singal where datime = (SELECT max(datime) FROM singal)')
    data = cur.fetchone()
    for da in data:
        ds.append(da)
    # print(type(ds))
    #转成str因为有数字所以这种写法
    li = ','.join('%s' %times for times in ds)
    # print(type(li))

    return li

    cur.close()
    conn.close()


def insert(cur, sql, args):
    try:
        cur.execute(sql, args)
    except Exception as e:
        # print(e)
        pass

def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='gbk') as f:
        reader = csv.reader(f)
        # head = next(reader)
        # print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into singal values(%s,%s,%s)'
        for item in reader:
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)


    conn.commit()
    cur.close()
    conn.close()


def csv_del():
    f = open(r"C:\EATEMP\开仓信号.csv")
    f.close()


while True:
# if __name__ == '__main__':
#     read_csv_to_mysql(r"C:\EATEMP\开仓信号.csv")
#     read_conn()
#     jttq()
    rec()
    listen()
    # read_yuyin()



import pymysql
import pyttsx3
import csv
import codecs
from aip import AipSpeech
from datetime import datetime

import speech_recognition as sr
import re
en = pyttsx3.init()

APP_ID = '16650822'
API_KEY = '5DOXosjtN8NxG5wlF0C4wIzm'
SECRET_KEY = 'oCSfGx5iKBLFzpQHoag7AfgKw0jlBnht'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 图灵
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
    gw = sj_su[144:155]
    dw = sj_su[162:168]
    fx = sj_su[173:186]
    hz = sj + gw + dw + fx
    return hz

# 播放
def listen():
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1536,
    })

    result_text = result["result"][0]

    print("问:" + result_text)

    if '名字' in result_text:
        rate = en.getProperty('rate')
        en.setProperty('rate', rate - 50)
        text = '斯乌爱帅 帅哥'
        en.say(text)
        print('答',text)
        en.runAndWait()
    elif '明天' in result_text:
        text = '明天是七月二号'
        en.say(text)
        print('答',text)
        en.runAndWait()
    elif '后天' in result_text:
        text = '后天是七月四号'
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
    elif '数据' in result_text:
        text = read_conn()
        en.say(read_conn())
        print('答',text)
        en.runAndWait()


    return result_text




def get_conn():
    db = pymysql.connect(host="localhost",port=3306,
                   user="root",password="root",
                   db="article",charset="gbk")
    return db

#按照时间排列最新数据
def read_conn():
    ds = []
    dt = []
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT name,MAX(datime),text from singal')
    data = cur.fetchone()
    for da in data:
        ds.append(da)
    # print(type(ds))
    li = ','.join('%s' %times for times in ds)
    # print(type(li))
    if li[0:6] == 'USDCHF':
        li = '美元'+ li[6:]

    elif li[0:6] == 'ASDCHF':
        li = '日元'+ li[6:]

    return li

def insert(cur, sql, args):
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)
            # db.rollback()

def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='gbk') as f:
        reader = csv.reader(f)
        head = next(reader)
        # print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into singal values(%s,%s,%s)'
        sqls = 'select * from singal '
        for item in reader:
            # if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
            #     continue
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)


    conn.commit()
    cur.close()
    conn.close()
'''
        if each[0] == 'USDCHF':
            each[0] = '美元'
        elif each[0] == 'GBPUSD':
            each[0] = '镑美'
        elif each[0] == 'ASDCHF':
            each[0] = '日元'
        elif each[0] == 'BBPUSD':
            each[0] = '韩元'
        elif each[0] == 'CBPUSD':
            each[0] = '欧元'
        elif each[0] == 'DSDCHF':
            each[0] = '黄金'
        elif each[0] == 'EBPUSD':
            each[0] = '钻石'
        elif each[0] == 'FBPUSD':
            each[0] = '人民币'
'''


while True:
# if __name__ == '__main__':
    read_csv_to_mysql(r"C:\Users\Administrator\Desktop\python\开仓信号.csv")
    read_conn()
    jttq()
    rec()
    listen()

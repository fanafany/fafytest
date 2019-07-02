import time
import csv
import pyttsx3
import itertools
import math
from datetime import datetime


#时间操作取最近的：
def data_time():
    #打开csv
    f = open('C:\\Users\Administrator\Desktop\python\开仓信号.CSV', 'r', newline='')
    reade = csv.reader(f)

    da_time = []
    de_time = []
    #初始化
    en = pyttsx3.init()
    for each in reade:
        if each[0] == 'USDCHF':
            each[0] = '美'
        elif each[0] == 'GBPUSD':
            each[0] = '明'
        elif each[0] == 'ASDCHF':
            each[0] = '元'
        elif each[0] == 'BBPUSD':
            each[0] = '韩'
        elif each[0] == 'CBPUSD':
            each[0] = '欧'
        elif each[0] == 'DSDCHF':
            each[0] = '黄'
        elif each[0] == 'EBPUSD':
            each[0] = '石'
        elif each[0] == 'FBPUSD':
            each[0] = '金'
        li = ','.join(each)
        # name = li[0]
        times = li[2:-7]
        si = min(times)


        # print(type(each[1]))

    print(li)
    if li.find('出现'):
        en.say('出现做空')
        en.runAndWait()
    else:
        en.say('不为空')
        en.runAndWait()



        # sorted(da_time,key=da_time[])
    # print(da_time)









    # print('最近时间：',da_time)
    # en.say(da_time)
    # en.runAndWait()
    # return data_time




if __name__ == "__main__":
    data_time()


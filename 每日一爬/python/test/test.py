import time
import csv
import math
import pymysql
import pyttsx3
from datetime import datetime
f = open('C:\\Users\Administrator\Desktop\python\开仓信号.CSV','r',newline='')
reade = csv.reader(f)
year, month, day, hour, minute, second, *_ = datetime.now().timetuple()
import datetime
dt = datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')
#时间操作取最近的：
da_time = []
dou = []
# en = pyttsx3.init()
for each in reade:
    # print(each)
    name,date_time,text = each
    da_time.append(each)
    from datetime import datetime
    # date_time = datetime.datetime.strptime(date_time,"%Y.%m.%d %H:%M:%S")

    a2time = time.mktime(time.strptime(date_time, '%Y.%m.%d %H:%M:%S'))
    dou.append(a2time)
    dou.sort()
    dou1 = time.strftime("%Y.%m.%d %H:%M:%S", dou)
# print(dou)
print(dou1)
# for i in a2time:
#     print(i)
# print(a2time)
# a1ti = min(da_time)
# print('最小值:',a1ti)

    # print('当前时间：',a1time)
    # year1, month1, day1, hour1, minute1, second1,*__ = date_time.timetuple()

    # if year1 == year and month1 == month and day1 == day:
    #     if hour1 < hour:
    #
    #         hour = min(hour,hour1)
    #         print(hour)


    #     print(name,date_time,text)
    # else:
    #     pass
# print(year1,month1,day1,hour1,minute1,second1)
# print(type(sou))

import datetime
d1 = datetime.datetime.strptime('2015-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2015-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
# print(delta.days)
# print(name,date_time,text)


noa = 2019
nob = 6
noc = 28
nod = 20
noe = 52
nof = 20




# def time_cmp(first_time, second_time):
#     print(first_time)
#     print(second_time)
#     return int(time.strftime("%H%M%S", first_time)) - int(time.strftime("%H%M%S", second_time))
# print(time_cmp(time.gmtime(), time.strptime("11:35:10", "%H:%M:%S")))
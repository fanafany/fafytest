import pyttsx3

import csv
f = open('开仓信号.CSV','r',newline='')
reade = csv.reader(f)
for no in reade:
    # print(no)
    if no[0] == 'USDCHF':
        no[0] = '美元'
    elif no[0] == 'GBPUSD':
        no[0] = '镑美'
    print(no)
    en = pyttsx3.init()
    rate = en.getProperty('rate')
    en.setProperty('rate',rate-5)
    en.say(no)
    if no[2]=='出现做空信号':
        en.say('建议做空')
    en.runAndWait()


    # en.say('GBPUSD')
    # en.say('you are pig.')



import pandas as pd
# import csv
# f = open('开仓信号.CSV','r',newline='')
# reade = csv.reader(f)
# for no in reade:
#     print(no)
# f.close()

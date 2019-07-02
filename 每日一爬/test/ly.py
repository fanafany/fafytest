from aip import AipSpeech
import pyttsx3
import csv
APP_ID = '16098023'                        #百度账号
API_KEY = 'deSRMmEmN0af41udWXZlOva1'
SECRET_KEY = 'mFGmZnjKRwL1wEiWGSx5eUadMB7UypHg'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
en = pyttsx3.init()

f = open('开仓信号.CSV', 'r', newline='')
reade = csv.reader(f)
def listen():
    with open('1642.wav', 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1536,
    })

    result_text = result["result"][0]

    print("you said: " + result_text)

    if str(result_text.find('做空')):
    # if str('呵呵' in result_text):

        for nos in reade:
            en.say()


    else:
        str(result_text.find('现在'))
        en.say('随便')
        en.runAndWait()
def sou():

    en.say('哈哈')
    en.runAndWait()

    return en

listen()
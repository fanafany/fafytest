import time
import os
import pyaudio
import wave
import datetime
import speech_recognition as sr
from aip import AipSpeech
import pygame
import requests
import json
import random
import pyttsx3
import csv

APP_ID = '16098023'                        #百度账号
API_KEY = 'deSRMmEmN0af41udWXZlOva1'
SECRET_KEY = 'mFGmZnjKRwL1wEiWGSx5eUadMB7UypHg'
flag=20
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#录音
def rec(rate=16000):
    global flag
    flag=1
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio = r.listen(source)
    with open(time1_str+".wav", "wb") as f:
        f.write(audio.get_wav_data())

def check(i):   #识别失误检测
    if i>=3301:
        if i<=3312:
            print("未检测到任何声音 \n")
            os._exit(1)

def listen():
    with open(time1_str+".wav", 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1536,
    })
    check(result['err_no'])
    result_text = result['result'][0]
    print("you said: " + result_text)

    return result_text


def riddle():
    f = open('开仓信号.CSV', 'r', newline='')
    reade = csv.reader(f)
    for no in reade:
        print(no)
        en = pyttsx3.init()
        en.say(no)
        if no[2] == '出现做空信号':
            en.say('建议做空')
        en.runAndWait()

def search():
    global flag
    flag=0

while True:
    time1 = datetime.datetime.now()
    time1_str = datetime.datetime.strftime(time1, '%H%M')  # 获取系统时间
    rec()
    listen()
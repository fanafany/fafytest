import pymysql
import pyttsx3
from aip import AipSpeech
from datetime import datetime

import speech_recognition as sr
import re
en = pyttsx3.init()
APP_ID = '16650822'
API_KEY = '5DOXosjtN8NxG5wlF0C4wIzm'
SECRET_KEY = 'oCSfGx5iKBLFzpQHoag7AfgKw0jlBnht'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

with open('recording.wav', 'rb') as f:
    audio_data = f.read()

result = client.asr(audio_data, 'wav', 16000, {
    'dev_pid': 1536,
})

result_text = result["result"][0]

print("问: " + result_text)
gou = result_text
if '今天' in result_text:
    text = '今天是七月二号'
    en.say(text)
    print('答:',text)
    en.runAndWait()
# if result_text == '今天':
#     en.say('今天是七月二号')
#     en.runAndWait()
if gou.find('今天'):
    en.say('今天天气很好！')
    print(en)
    en.runAndWait()
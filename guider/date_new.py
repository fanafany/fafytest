# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-09-11 15:10 '
import pymysql
import pyaudio
from aip import AipSpeech
import speech_recognition as sr
import wave
import os
import time
import requests
import json

APP_ID = '16650822'
API_KEY = '5DOXosjtN8NxG5wlF0C4wIzm'
SECRET_KEY = 'oCSfGx5iKBLFzpQHoag7AfgKw0jlBnht'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

TURING_KEY = "311b0cd44df6401d8c3045518109a959"
URL = "http://openapi.tuling123.com/openapi/api/v2"
HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}



def rec(rate=16000):  # 最大的采样率
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())

    return  audio

def check_mis(i):  # result  err_on的返回值  有错误退出防止程序错误
    if i == 3301:
        # QMessageBox.about(self, '  ',"音频质量过差")
        # print("音频质量过差")
        return 1

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



    return result_text


def speak(text=""):
    result = client.synthesis(text, 'zh', 1, {
        'spd': 4,
        'vol': 5,
        'per': 4,
    })

    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)

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

def play():
    os.system('sox audio.mp3 audio.wav')
    wf = wave.open('audio.wav', 'rb')
    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()

while True:
    rec()
    request = listen()
    response = robot(request)
    speak(response)
    play()
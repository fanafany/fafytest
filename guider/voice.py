# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-09-11 14:37 '

import speech_recognition as sr

def rec():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2, sample_rate=44100,chunk_size=512) as source:
        print("请说话:")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())

    return  audio
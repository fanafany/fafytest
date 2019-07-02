import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QMovie, QPainter, QPalette, QBrush, QPixmap
from random import randint
import speech_recognition as sr
import os
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import ctypes
import time
from PyQt5.QtCore import *

"""
# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
try:
    print("You said " + recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))"""
# 转战百度


from aip import AipSpeech

APP_ID = '16650822'
API_KEY = '5DOXosjtN8NxG5wlF0C4wIzm'
SECRET_KEY = 'oCSfGx5iKBLFzpQHoag7AfgKw0jlBnht'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_wav(rate=16000):  # 最大的采样率
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        # print("please say something")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:  # 这里会在子目录创建一个wav格式的音频文件
        f.write(audio.get_wav_data())  # 将声音文件存储子在recording.wav里


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


def change_wav():
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()
    result = client.asr(audio_data, 'wav', 16000, {'dev_pid': 1737, })  # 识别本地文件存储的wav
    i = result['err_no']

    # switch(i)

    j = check_mis(i)
    if j == 1:
        return 1  # 0是正常的返回值
    text = result['result'][0]  # 返回音频质量 错误码 错误码描述

    # print("you said: " + text)

    return text


class main(QWidget):
    def closeEvent(self, event, where=1):  # 关闭窗口事件
        if where != 1:
            # reply = QMessageBox.question(self, '确认', '请退出重试', QMessageBox.Yes)
            event.accept()
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)  # 两个no  取消按钮高亮挽留使用者啊
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        # self.setStyleSheet("background-color:\play.gif;")
        # self.setBackgroundRole(QPalette.setBrush(QPalette.Background,QBrush(QPixmap(":/background.png"))))
        # self.setAutoFillBackground(True)

        # self.setPalette(QPalette(Qt.yellow))
        self.setGeometry(500, 300, 280, 400)  # //界面位置和图标
        self.setWindowTitle('精简版语音交互')
        self.setWindowIcon(QIcon('image\图标.ico'))
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('image\play.gif')

        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)

        hbox.addWidget(lb1)
        self.setLayout(hbox)

        self.move(800, 300)  # 窗口的位置

        self.bt1 = QPushButton(QIcon('image\play.gif'), '录音', self)
        # self.setStyleSheet(QPushButton(":\\"))
        self.bt1.setGeometry(100, 350, 70, 30)  # 录音图标位置
        self.bt1.clicked.connect(self.start_listen)
        self.bt1 = QPushButton(QIcon('image\mp3.png'), '', self)
        self.bt1.setGeometry(45, 350, 30, 30)
        self.bt1.clicked.connect(self.start_mic)
        self.bt1 = QPushButton(QIcon('txt.png'), '', self)
        self.bt1.setGeometry(195, 350, 30, 30)
        self.bt1.clicked.connect(self.start_txt)
        self.show()

    def start_mic(self):
        os.system('dvdplay')

    def start_txt(self):
        os.system('notepad')

    def start_listen(self):
        get_wav()  # 完成录音文件
        QMessageBox.about(self, '  ', '识别完成')
        if change_wav() == 1:  # 此函数 中途 改变返回值   非正常返回
            QMessageBox.about(self, '  ', "未识别到任何声音，请退出重试 ")
            self.closeEvent(self, 2)  # 强制退出
        text = change_wav()
        if text == 'play' or text == 'music' or text == 'play music':
            os.system('dvdplay')
        elif text == 'open' or text == 'notepad' or text == 'open notepad':
            os.system('notepad')
        else:
            QMessageBox.about(self, '  ', "无可执行指令\"" + str(text) + "\"")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())
    input();

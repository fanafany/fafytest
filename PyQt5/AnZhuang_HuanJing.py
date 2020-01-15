#!/usr/bin/env python3
# coding: utf-8

import os,sys,re
try :
	path = os.path.dirname(sys.argv[0])#把脚本所在目录直接终端运行
	os.chdir(path)
except:pass



if sys.platform =="win32":
    biao=[

    "pygame==1.9.4",
    "qrcode==6.1",
    "image==1.5.2",
    "requests==2.21.0",
    "psutil==5.6.1",
    "pynput==1.4",
    "PyAudio==0.2.11",
    "PyInstaller==3.5",
    "pyautogui==0.9.30",
    "keras==2.2.4",
    "Pillow==6.1.0",
    "matplotlib==3.0.3", 
    "tensorflow==1.5.0",
    "python_speech_features"
    #"tensorflow==1.12.0"

    ]
else:
    
    
    biao=[

    "pygame==1.9.6",
    "qrcode==6.1",
    "image==1.5.2",
    "requests==2.21.0",
    "psutil==5.6.1",
    "pynput==1.4",
    #PyAudio==0.2.11",
    "PyInstaller==3.3",
    "pyautogui==0.9.30",
    "keras==2.2.4",
    "Pillow==6.1.0",
    "matplotlib==3.0.3",
    "tensorflow==1.5.0",
    "python_speech_features"
    #"tensorflow==1.12.0"
    ]
#     if os.popen("cat /proc/cpuinfo | grep model").read().count("Pentium") >=1:
#         biao.append("tensorflow==1.5.0")
#     else:
#         biao.append("tensorflow==1.12.0")
if sys.platform !="win32":
    os.system("sudo apt-get install python3-pip -y")
    os.system("sudo apt install python3-tk=3.5.3-1 -y")
    os.system("sudo apt-get install python3-pyaudio=0.2.11-1 -y")
    #os.system("sudo apt-get install python3-pil python3-pil.imagetk -y")

for x in biao:
    if sys.platform =="win32":
        os.system("pip install {} -i https://pypi.tuna.tsinghua.edu.cn/simple".format(x) )
    else:
        os.system("sudo pip3 install {} -i https://pypi.tuna.tsinghua.edu.cn/simple".format(x) )
    print('----------------->ok',x)
input("回车确认安装完成")

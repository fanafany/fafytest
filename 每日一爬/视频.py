import requests
from fake_useragent import UserAgent
import time

ua = UserAgent() #随记生成User-Agent

def downloads(url,path):
    #开始下载的时间
    start = time.time()
    size = 0

    headers = {
        "User-Agent": ua.random
    }

    # stream 属性必须带上
    response = requests.get(url,headers=headers,stream=True)
    # print(response)
    #每次下次的数据大小
    chunk_size = 1024
    #视频总大小
    content_size = int(response.headers["content-length"])

    if response.status_code == 200:
        #文件读写
        with open(path,"wb") as f:
            #l浏览器发送给数据的数据
            for data in response.iter_content(chunk_size=chunk_size):
                #获取到的数据写入
                f.write(data)
                #已经下载的文件大小
                size += len(data)
                #进度条
                print("\r"+"[下载进度]：%s%.2f%%" %(">"*int(size * 50 / content_size),float(size / content_size * 100)),end= " ")
        #结束时间
        end = time.time()

        print("\n"+"视频下载完成 用时：{}".format(end - start))

def Thje_url(page):
    "通过API获取到视频的详细信息"
    uri = "http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc"
    url = "http://api.vc.bilibili.com/board/v1/ranking/top?page_size={}&next_offset=&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc".format(page)

    #模拟用户请求；添加请求头User-Agent
    headers = {
        "User-Agent": ua.random
    }

    #模拟用户请求网页
    sponse = requests.get(url,headers=headers).json()
    #通过data来取到最终的视频原址连接
    item = sponse.get("data").get("items")
    # print(item)
    for i in item:
        #得到item对应数据
        ite = i.get("item")
        # print(ite)
        #获取到视频标题
        Video_name = ite.get('description')
        #视频发布日期
        Video_time = ite.get('upload_time')

        #视频播放地址
        Video_bofang = ite.get('share_url')

        #视频下载地址
        Video_download = ite.get('video_playurl')

        #视频作者
        The_name = i.get('user').get('name')

        #获取到Url用来下载视频
        try:
            print("当前下载的是{}".format(Video_name))
            downloads(Video_download,path="{}.mp4".format(Video_name))
        except Exception as e:
            print(e)

for page in range(1,10):
    page += page * 10 + 1
    Thje_url(page)
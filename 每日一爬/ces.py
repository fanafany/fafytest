from lxml import etree
from OpenSSL import SSL
import requests
import re
import time
import os

HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'Referer': 'http://www.mzitu.com'
}
QUANTITY =225#图集页数  每页/24

FILE_PATH = None #下载路径，请设置绝对路径，默认以当前绝对路径做保存



def get_path(name,num=" "):
    '''
    当num为None时，用来查询目录是否存在
    :param name:
    :param num:
    :return:
    '''
    currrent_path = os.path.realpath(__file__)  # 文件绝对路径
    current_dir = os.path.split(currrent_path)[0]
    file_path = os.path.join(current_dir, name)
    if num==" ":
        if not os.path.exists(file_path):
            return False
    if FILE_PATH is None:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    else:
        file_path = FILE_PATH
    return os.path.join(file_path,num) + ".jpg"

def get_response(url):
    """返回URL响应"""
    time.sleep(2)
    return requests.get(url=url,headers=HEADERS)

def atlas():
    '''
    :yield:图集下载的地址
    '''
    for i in range(QUANTITY):
        url = "https://www.mzitu.com/page/{page}/".format(page=i)
        response = get_response(url=url).text
        imgurl_list = re.findall(r'<li><a href="(.*?)" target="_blank">',response)
        imgname_list = re.findall(r"alt='(.*?)' width=",response)
        for img_naem,img_url in zip(imgname_list,imgurl_list):
            item = {}
            item["name"] = img_naem
            print(img_naem)
            # if not get_path(name=img_naem):
            #     break
            item["img_url"] = img_url
            yield item


def get_download_url(item):
    """
    :param url:图片url
    :return:  图集下载地址
    """
    response = get_response(url=item["img_url"]).text
    etre = etree.HTML(response)
    num = etre.xpath("//div[@class='pagenavi']/a[5]/span/text()")
    for i in range(0,int(num[0])+1):
        item["download"] = item["img_url"]+ "/" + str(i)
        item["number"] = str(i)
        yield item


def download(item):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'Referer': item["download"]
    }
    try:
        time.sleep(2)
        etre = etree.HTML(requests.get(url=item["download"],headers=headers).text)
        download_url = etre.xpath("//div[@class='main-image']/p/a/img/@src")[0]
        response = requests.get(url=download_url,headers=headers).content
        file_path = get_path(item["name"],item["number"])
        with open(file_path,"wb") as fp:
            fp.write(response)
    except SSL.SysCallError as e:
        # print("当前出现错误%s"%e)
        # print(item)
        pass



def product(c):
    c.send(None)
    for img in atlas():
        c.send(img)
    c.close()


def customer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        for each in get_download_url(item=n):
            download(each)

def main():
    func = customer()
    product(func)


if __name__ == '__main__':
    main()
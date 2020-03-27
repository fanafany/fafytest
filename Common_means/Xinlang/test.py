# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-27 11:47 '
import requests
from lxml import etree
url = 'https://med.sina.com/article_list_-1_1_1_4126.html'
header = {
    'authority':'med.sina.com',
    'method':'GET',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'cookie':'route=68330abb7d350cd7d4a7b25d00326afb; JSESSIONID=AF779972B80E6C8315D0041FA1F82DC2-node1.front_1; Hm_lvt_c17ba36cc47e6c7f6d03dc1ce7bc7c84=1585280040; Hm_lpvt_c17ba36cc47e6c7f6d03dc1ce7bc7c84=1585286301',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
# url = 'https://www.taobao.com'
req = requests.get(url=url,headers=header,verify=False)
req.encoding = 'utf-8'
print(req.text)
# htmls = etree.HTML(req.text)
# content = htmls.xpath("//div[@class='article']/p/text()")
# contents = ''.join(content)
# datime = htmls.xpath("//div[@class='date-source']/span[1]/text()")
# datimes = ''.join(datime)
# print(contents)
# print(datimes)
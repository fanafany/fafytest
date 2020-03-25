import requests
from lxml import etree
import json
url = 'http://health.people.com.cn/GB/408572/index.html'
header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
response = requests.get(url,header)
response.encoding = "gb2312"
html = etree.HTML(response.text)
urls = html.xpath('//div[@class="newsItems"]/a/@href')
dics = []
for i in urls:
    item = 'http://health.people.com.cn'+i
    res = requests.get(item,header)
    res.encoding = 'gb2312'
    htmls = etree.HTML(res.text)
    title = htmls.xpath("//div[@class='title']/h2/text()")
    titles = ''.join(title)
    content = htmls.xpath("//div[@class='artOri']/text()".replace('来源：',''))
    conts = ''.join(content)
    laiy = htmls.xpath("//div[@class='artOri']/a/text()")
    laiys = ''.join(laiy)
    contents = htmls.xpath("//div[@class='artDet']/p/text()")
    contems = ''.join(contents)
    dic = {
        "title":titles,
        'time':conts,
        'fcount':item,
        'keywords':laiys,
        'message':contems
    }
    dics.append(dic)

# print(dic)
with open('data.json','w',encoding='utf-8')as file:
    file.write(json.dumps(dics,indent=2, ensure_ascii=False))

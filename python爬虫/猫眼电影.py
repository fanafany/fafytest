import requests
import re
import json
import multiprocessing
from requests import RequestException
import pymysql
conn = pymysql.connect(
    host='localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'pysql_demo',
    charset = 'utf8'
)
cursor = conn.cursor()
#抓取完整网页
def get_html(url):
    try:
        response = requests.get(url)
        return response.text
    except RequestException:
        return None
#正则解析提取电影信息，用yield构造生成器对象
def parse_html(html):
    patter = re.compile('<dd>.*?board-index.*?(\d+).*?data-src="(.*?)".*?name"><a href="(.*?)" title="(.*?)" .*?movieId:(.*?)}">.*?</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S)
    movie_list = re.findall(patter,html)
    dy_st = 'https://maoyan.com'
    for item in movie_list:
        #数据库存入写法：
        cursor.execute(
            "insert into pysql_demo(ranking,movie_id,movie_title,imgurl,movie_url,actor,showtime,grade)values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(item[0],item[4],item[3],item[1],dy_st+item[2],item[5],item[6],item[7]+item[8]))
        conn.commit()
        yield {
            "排名": item[0],
            "封面链接": item[1],
            "电影链接":dy_st+item[2],
            "电影名":item[3],
            "电影id":item[4],
            "主演：":item[5].strip(),
            "上映时间":item[6],
            "评分：":item[7]+item[8]

        }

#将提取到的信息格式化为json文件
def write_to_file(text):
    with open('moviestop100.txt','a',encoding='utf-8')as f:#保存本地
        f.write(json.dumps(text,ensure_ascii=False)+'\n')

#主方法，构建请求URL，并实现单个页面网页的提取
def main(i):
    url = 'http://maoyan.com/board/4?offset='+str(i)
    html = get_html(url)
    for item in parse_html(html):
        print(item)
        # f.write(item)


#程序执行的入口，创建一个进程池对象，并使用map函数实现多进程
if __name__ == '__main__':
    #多进程方式：
    # pool = multiprocessing.Pool()
    # pool.map(main,[i*10 for i in range(12)])

    #正常方式：
    for i in range(10):
        main(i*10)

    conn.close()
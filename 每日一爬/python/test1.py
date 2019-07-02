import pymysql
def get_conn():
    db = pymysql.connect(host="localhost",port=3306,
                   user="root",password="root",
                   db="article",charset="gbk")
    return db

def read_conn():
    ds = []
    dt = []
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT name,MAX(datime),text from singal')
    data = cur.fetchone()
    for da in data:
        ds.append(da)
    # print(type(ds))
    li = ','.join('%s' %times for times in ds)
    # print(type(li))
    if li[0:6] == 'USDCHF':
        li = '美元'+ li[6:]

    elif li[0:6] == 'ASDCHF':
        li = '日元'+ li[6:]
    # print(li)
    return li

    cur.close()
    conn.close()

def qwe():
    dew = read_conn()
    print(dew)
read_conn()
qwe()
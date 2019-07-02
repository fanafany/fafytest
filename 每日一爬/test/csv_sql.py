import pymysql
import csv
import codecs


def get_conn():
    db = pymysql.connect(host="localhost",port=3306,
                   user="root",password="root",
                   db="article",charset="gbk")
    return db


def insert(cur, sql, args):
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)
        # db.rollback()



def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='gbk') as f:
        reader = csv.reader(f)
        head = next(reader)
        print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into singal values(%s,%s,%s)'
        for item in reader:
            # if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
            #     continue
            args = tuple(item)
            print(args)
            insert(cur, sql=sql, args=args)

        conn.commit()
        cur.close()
        conn.close()



if __name__ == '__main__':
    read_csv_to_mysql(r"C:\Users\Administrator\Desktop\python\开仓信号.csv")

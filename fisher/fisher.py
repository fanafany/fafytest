# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-29 13:35 '

from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/hello')
def hello():
    return 'hello world'

# app.add_url_rule("/hello",view_func=hello)#同上面装饰器一样，路由注册

if __name__ == "__main__":
    #生产环境 nginx+uwsgi
    # app.run(host='192.168.1.118',debug=True)#指定具体的ip，这种如果有两个网卡就没办法了
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)#换成这种才是通用的本地都能访问,后面可指定端口也可不指定
    # app.run(debug=True)@debug只是在开发模式开启，真正上线时要取消，因为性能比较差
# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-13 15:05 '

import tornado.web

#定义一个首页的视图
class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("<h1>开发一个实时监控系统</h1>")
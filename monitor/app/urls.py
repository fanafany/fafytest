# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-13 14:54 '

from app.views.views_index import IndexHandler as index

#配置路由和视图的映射规则
urls = [
    (r"/",index)
]
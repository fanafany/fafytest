# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-12 10:29 '
#不建议继承list和dict
# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key,value*2)
#
# my_dict = Mydict(one = 1)#这种的它是没有调用里面的方法的
# my_dict["one"] = 1#这种的才调用了
# print(my_dict)
#
# #如果非要继承不要继承dict 而要继承下面这个模块里的UserDict
# from collections import UserDict
#
# class Mydict(UserDict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key,value*2)
#
# my_dict = Mydict(one = 1)#这种就为2了
# # my_dict["one"]
# print(my_dict)

from collections import defaultdict

my_dict = defaultdict(dict)
my_value = my_dict["bobby"]#为空不存在

pass

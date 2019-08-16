# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-15 10:54 '

#python中垃圾回收的算法是采用引用计数
a = object()
b = a
del a
print(b)
print(a)

#python里有个魔法函数也可实现垃圾回收,可在类里实现然后重载它
class A:
    def __del__(self):
        pass
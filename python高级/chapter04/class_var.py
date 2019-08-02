# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-07-31 15:28 '

class A:
    aa = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y

a = A(2,3)

A.aa = 11#改变类的变量
a.aa = 100
print(a.x,a.y,a.aa)
print(A.aa)#11

b = A(3,5)
print(b.aa)#11





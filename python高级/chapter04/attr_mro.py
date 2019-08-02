# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-01 10:45 '

#新式类，也可这种写法：
#class D(object):#写不写都可以
class D:
    pass

class E:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B,C):
    pass

print(A.__mro__)#继承mro变量
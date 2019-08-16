# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-15 10:36 '

#python和java中的变量本质不一样，python的变量实质上是一个指针int str，便利贴

a = 1
a = 'abc'
#1.a贴在1上面
#2.先生成对象，然后贴便利贴
'''
== 用于判断是否同一个值
is 是否同一个类型
'''

a = [1,2,3]
b = a
print(id(a),id(b))
print(a is b)
b.append(4)
print(a)

a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(id(a),id(b))#同样的值但赋给另外一个变量就是不同的
print(a is b)

class People:
    pass
person = People()
if type(person) is  People:
    print(type(person))
    print(person)
    print("yes")
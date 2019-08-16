# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-07 15:44 '

my_list =[]
my_list.append(1)
my_list.append("a")

from collections import abc

a = [1,2]
c = a + [3,4]

#就地加
a += (5,6)
# a += [5,6]#这样写也可以，而上面的 直接+就会报错，必须list

a.extend(range(3))#extend是迭代的方式
a.append([7,8])#append传入的是一个数值，不是迭代的方式
print(a)
# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-08 17:56 '

#array,deque
#数组
#这两个都比list效率高
import array
#array和list的一个重要区别，array只能存放指定的数据类型（同一个数据类型）
my_array = array.array("i")
my_array.append(1)
my_array.append("abc")
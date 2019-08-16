# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-12 10:43 '

#set 集合fronzenset(不可变集合)无序，不重复，去重常用
# s = set('abcdeff')
# s = set(['a','b','c','d','e'])
# s = {'a','b'}
# s.add('c')
# print(s)
#
# s = frozenset('abcde')#设置好无法修改，无法添加值，它是个不可变的类型，可以作为dict的key使用
# print(s)

#向set添加数据
s = {'a','b','c'}
another_set = set("cef")
re_set = s.difference(another_set)
re_set = s - another_set #求差集
re_set = s & another_set #交集
re_set = s | another_set#并集
print(re_set)

#set 性能很高 时间复杂度为1  直接计算的

#set判断
print(s.issubset(re_set))
if "c" in re_set:
    print("i am set")

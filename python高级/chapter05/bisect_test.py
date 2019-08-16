# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-08 17:39 '

import bisect
from collections import deque

#用来处理已排序的序列，用来维持已排序的序列，升序
#二分查找
inter_list = []
#用deque也可以
# inter_list = deque()
bisect.insort(inter_list,3)
bisect.insort(inter_list,2)
bisect.insort(inter_list,5)
bisect.insort(inter_list,4)
bisect.insort(inter_list,1)
bisect.insort(inter_list,6)

#位置
print(bisect.bisect_right(inter_list,3))

print(inter_list)
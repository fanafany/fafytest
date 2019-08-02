# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-07-31 15:03 '

#使用isinstance判断类型而不是type判断

class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b,B))#True
print(isinstance(b,A))#True


#显然两个ID是不相等的，得用isinstance才行
print(type(b)is A)#False
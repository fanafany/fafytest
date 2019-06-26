
#返回一个数字的绝对值。参数可以是整数或浮点数。如果参数是复数，则返回其大小。
#注：不可传多个
print(abs(100))
print(abs(1.5))
print('***********')

#max函数可以接收多个参数，并返回最大的那个：
print(max(1,3))
print(max(3,2,-3,4,12))
print('***********')
#数据类型转换
print(int('123'))#123
print(int(12.34))#12

print(float('12.34'))#12.34

print(str(1.23))
print(str(100))

print(bool(1))
print(bool(''))
print('***********')

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
abs(100)
a = abs
print(a(-1))
print('***********')
n1 = 255
n2 = 1000
print(hex(n1)+'\n'+hex(n2))





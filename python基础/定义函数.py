

#python中定义一个函数使用def，函数返回值用return
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# print(my_abs(2))
#注：如果传入的类型或者参数个数不对都会抛错

#数据类型检查可以用内置函数isinstance()实现,只允许整数和浮点数：
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("type error")
    if x >= 0:
        return x
    else:
        return -x
# print(my_abs(5.2))

#函数返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x,y = move(100,100,60,math.pi/6)
# print(x,y)
#但是这只是一个假象使用print（x）单个返回的值也还是一样的
#注：原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，
# Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


#空函数，什么都不做可以使用pass语句
def pop():
    pass
#pass语句可以用来当作占位符，先让程序运行起来，比如：
age = 5
if age >= 22:
    pass


#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax2+bx+c=0 的两个解。
import math
def quadratic(a,b,c):
    ma = b**2-4*a*c
    if not isinstance(a+b+c,(int,float)):
        raise TypeError('type error!')
    elif ma<0:
        return '无解'
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
print(quadratic(1,3,2))

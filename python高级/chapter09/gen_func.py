# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-21 14:08 '

#生成器函数，函数里只要有yield关键字
#正常函数只能返回一个return，多写几个也是无效的，而生成器yield可多写
def gen_func():
    yield 1
    yield 2
    yield 3

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):#用list如果数增加就会占内存
    re_list = []
    a,b,c = 0,0,1
    while a<index:
        re_list.append(c)
        b,c = c,b+c
        a += 1
    return re_list

def gen_fib(index):#生成器的方式
    a,b,c = 0,0,1
    while a<index:
        yield c
        b,c = c,b+c
        a += 1
for date in gen_fib(10):
    print(date)

# print(fib(10))
# print(fib2(10))

#斐波拉契算法（就是后一个数是前两个数的和）0 1 1 2 3 5 8 13
#惰性求值，延迟求值 提供了可能

def func():
    return 1

if __name__ == "__main__":
    #生成器对象,python编译字节码的时候就产生了
    gen = gen_func()
    # for value in gen:
    #     print(value)
    # re = func()
    # pass
# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-09 9:15 '

#列表生成式（列表推导式）
#1.提取出1-20之间的奇数
odd_list = []
for i in  range(21):
    if i%2 == 1:
        odd_list.append(i)

#同下：
odd_list = [i for i in range(21) if i % 2 == 1]

#2.逻辑复杂的情况
def handle_item(item):
    return item * item
odd_list = [handle_item(i) for i in range(21) if i % 2 == 1]
#列表生成式性能高于列表操作
print(odd_list)

#生成器表达式
odd_list = (i for i in range(21) if i % 2 == 1)
print(type(odd_list))

for item in odd_list:#通过for循环打印生成器
    print(item)

odd_gen = (i for i in range(21) if i % 2 == 1)
print(type(odd_list))
odd_list = list(odd_gen)
print(type(odd_list))
print(odd_list)

#字典推导式
my_dict = {"fana":12,"fana1":13,"fana2":14}
revered_dict = {value:key for key,value in my_dict.items()}
print(revered_dict)

#集合推导式
# my_set = set(my_dict.keys())
#上面的方法也可以  刚好有这个keys方法，但下面效率更高还可加入自己逻辑
my_set = {key for key,value in my_dict.items()}
print(type(my_set))
print(my_set)
# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-07 9:46 '

#自省是通过一定的机制查询到对象的内部结构
from chapter04.class_method import Date
class Person:#文档
    """
    人
    """
    name = 'user'

class Student(Person):
    def __init__(self,school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("fanafany")

    #通过__dict__查询属性
    print(user.__dict__)#{'school_name': 'fanafany'}
    print(Person.__dict__)
    print(user.name)#user

    #也可通过直接取
    user.__dict__["school_addr"] = "江苏"
    print(user.school_addr)#江苏

    #dir 可列出对象所有属性,dir比上面的dict更加强大
    print(dir(user))
    #列如：
    a = [1,2]
    print(dir(a))#用上面的dict会报错  而用dir可直接用
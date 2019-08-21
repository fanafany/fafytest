# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-16 10:02 '

#类也是对象，type创建类的类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

#type动态创建类
# User = type("User",(),{})
def say(self):
    return 'i am user'

class BaseClass:
    def answer(self):
        return 'i am baseclass'

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args,**kwargs)

#什么是元类，元类是创建类的类，对象<-class（对象）<-type
class User(metaclass=MetaClass):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "user"

if __name__ == "__main__":
    # Myclass = create_class("user")
    # my_obj = Myclass()
    # print(type(my_obj))
    # User = type("User", (BaseClass,), {"name":"user",'say':say})
    my_obj = User(name="fanafany")
    print(my_obj)
    #6228210459030996073
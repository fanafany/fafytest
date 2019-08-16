# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-15 15:23 '
from datetime import date,datetime
class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0 #前面加下划线表示这个属性不想对外暴露，想让它通过方法，或者属性描述符的方式来访问
                     #但实际上除了双下划綫之外，它并不能够隐藏，只是说代码上英特规范而已

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    #动态属性property
    #装饰器:这种方法通过原先是取函数的方法，现在下面通过装饰器直接取属性的方式
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    #必须要对age这个字段进行设置：
    @age.setter
    def age(self,value):
        self._age = value



if __name__ == "__main__":
    user = User("fanafany",date(year=1998,month=1,day=12))
    user.age = 20
    print(user._age)#20
    print(user.age)#这边还是21，它是一个动态计算出来的
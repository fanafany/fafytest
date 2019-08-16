# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-15 15:46 '

#__getattr__,__getattribute__
#__getattr__就是在查找不到属性的时候调用
#__getattribute__无条件的进入

from datetime import date,datetime
class User:
    def __init__(self,name,birthday,info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        return "fany"

if __name__ == "__main__":
    user = User("fanafany",date(year=1998,month=1,day=12),info={"company_name":"fana"})
    print(user.company_name)
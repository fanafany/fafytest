# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-05 15:13 '

from chapter04.class_method import Date
class User:
    def __init__(self,birthday):
        self.__birthday = birthday

    def get_age(self):
        #返回年龄
        return 2019 - self.__birthday.year

if __name__ == "__main__":
    user = User(Date(1998,1,12))
    print(user._User__birthday)
    print(user.get_age())
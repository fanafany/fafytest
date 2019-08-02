# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-01 16:35 '

class Date:
    #构造函数：
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)

if __name__ == "__main__":
    new_day = Date(2019,8,1)
    new_day.tomorrow()
    print(new_day)

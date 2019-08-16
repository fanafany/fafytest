# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-07 17:12 '

import numbers
class Group:
    #支持切片操作
    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = group_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return  cls(group_name=self.group_name,company_name=self.company_name,staffs=self.staffs[item])


    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

staffs = ['fana','fany','fafy','fyfa']
group = Group(company_name="fana",group_name='user',staffs=staffs)
reversed(group)
for user in group:
    print(user)
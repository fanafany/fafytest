# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-15 13:44 '

def add(a,b):
    a += b
    return a

class Company:
    def __init__(self,name,staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self,staff_name):
        self.staffs.append(staff_name)
    def remove(self,staff_name):
        self.staffs.remove(staff_name)

if __name__ == "__main__":
    com1 = Company("com1",["bobby1","bobby2"])
    com1.add("bobby3")
    com1.remove("bobby1")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("bobby")
    print(com2.staffs)
    print(Company.__init__.__defaults__)

    com3 = Company("com3")
    com3.add("bobby5")
    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs)#因为它两都使用了默认的list
    #尽量不传递list，list传进来也是可被修改的



    # a = 1
    # b = 2
    # c = add(a,b)
    #
    # a = [1,2]
    # b = [3,4]
    # c = add(a, b)
    #
    # a = (1,2)
    # b = (3,4)
    # c = add(a, b)
    #
    #
    # print(c)
    # print(a,b)
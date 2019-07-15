class Company(object):
    def __init__(self,employee_list):
        self.employe = employee_list
    def __getitem__(self, item):
        return self.employe[item]
    def __len__(self):
        return len(self.employe)

company = Company(['fafy','fafy1','fafy2'])
#还可通过切片方法，但上面得有魔法函数才行

#调用上面的len魔法函数
print(len(company))

company1 = company[:2]
# emploee = company.employe
#本身如果直接遍历company 会报错说它是个不可迭代的
#可通过上面再定义一个魔法函数,可省略上面一步,变成一个可迭代的
for item in company1:
    print(item)


# class Company(object):
#     def __init__(self,employee_list):
#         self.employe = employee_list
#     def __str__(self):
#         return ",".join(self.employe)
#     def __repr__(self):
#         return ",".join(self.employe)
#
# company = Company(['fafy','fafy1','fafy2'])
#company#fafy,fafy1,fafy2
#company.__repr__()#'fafy,fafy1,fafy2'
class Cat(object):
    def say(self):
        print("i am a cat")

class Company(object):
    def __init__(self,employee_list):
        self.employe = employee_list

    def __getitem__(self, item):
        return self.employe[item]

    def __len__(self):
        return len(self.employe)

company = Company(['fafy','fafy1','fafy2'])

class Dog(object):
    def say(self):
        print("i am a dog")


class Duck(object):
    def say(self):
        print("i am a duck")



#都调用它的say方法，就可实现一个多态
animal_list = [Cat,Dog,Duck]
for animal in animal_list:
    animal().say()
#i am a cat
#i am a dog
#i am a duck


a = ['fafy1','fafy2']
b = ['fafy2','fafy']
name_tuple = ["fafy3","fafy4"]
name_set = set()
name_set.add("fafy5")
name_set.add("fafy6")
a.extend(company)#可迭代的对象  列表合并
print(a)
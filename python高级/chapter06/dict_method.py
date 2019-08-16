# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-12 9:19 '

a = {"bobby1":{"company":"fanafany"},
     "bobby2":{"company":"fanafany1"}
     }
#clear
# a.clear()
# pass

#copy,返回浅拷贝
# new_dict = a.copy()#浅拷贝它把a的值也变了，它们指向的是同一个值，所以不注意这很有可能是一个坑
# new_dict["bobby1"]["company"] = "fanafany3"
# pass

#深拷贝
import copy
#深拷贝a的值是没有被改变的
# new_dict = copy.deepcopy(a)
# new_dict["bobby1"]["company"] = "fanafany3"


#formkeys 把可迭代的对象转换成dict
new_list = ["bobby1","bobby2"]
new_dict = dict.fromkeys(new_list,{"company":"imooc"})

# new_dict["bobby"]#如果像这种它里面没有就会报一个keyError的错，找不到这个key，可通过下面get方法
# value = new_dict.get("bobby",{})#如果不存在就给它传空的值
# value = new_dict.get("bobby1",{})#如果有值则取出

# for key,value in new_dict.items():
#     print(key,value)

default_value = new_dict.setdefault("bobby","imooc")

#uqdate几种方式

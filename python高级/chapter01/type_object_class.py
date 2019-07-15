# a = 1
# b = 'abc'
# print(type(1))#int
# print(type(int))#type
# print(type(b))#str
# print(type(str))#str
#type->int->1

#type->class->obj
#object 是所有类都要继承的一个顶层的基类
#type也是一个类，同时type也是一个对象
print(type.__bases__)#(<class 'object'>,)
print(type(object))#<class 'type'>
print(object.__bases__)#最顶层基类为空，其它的最终都指向type
class Student:
    pass
class MyStudent(Student):
    pass
# stu = Student()
# print(type(stu))#<class '__main__.Student'>
# print(type(Student))#<class 'type'>

# print(Student.__bases__)#(<class 'object'>,)
# print(type(object))#<class 'type'>
#
# print(MyStudent.__bases__)#(<class '__main__.Student'>,)
# print(type(Student))#<class 'type'>




# a = [1,2]
# print(type(a))#<class 'list'>
# print(type(list))#<class 'type'>



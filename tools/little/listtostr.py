# _*_ coding: utf-8 _*_
__author__ = 'yubinquan'
__date__ = '2019/6/18 13:04'

class MyClass:
    data = 1


instance = MyClass()
print("myclass",MyClass)
print("instance",instance)
# 输出
# (__main__.MyClass, < __main__.MyClass instance at 0x7fe4f0b00ab8 >)
# instance.data
print(instance.data)
# 输出
# 1

MyClass = type('MyClass', (), {'data': 2})
instance = MyClass()
print("MyClass",MyClass)
print("instance",instance)
# 输出
# (__main__.MyClass, < __main__.MyClass at 0x7fe4f0aea5d0 >)

print(instance.data)# 输出

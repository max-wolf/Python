# -*- coding:utf-8 -*-

import datetime as dt
import time as tm

#自定义函数
# def myfoo():
#     pass #占位符
#
# myfoo()

#内置函数
# print(abs(-35))

#形参 函数接收的参数 my_a
#实参 实际接收的参数 -45
#返回参数 形参b 实参a
# def my_abs(my_a):
#     if my_a >= 0:
#         b = my_a
#     else:
#         b = -my_a
#     return b
#
# a = my_abs(-45)
# print(a)

#位置参数/必须参数
# def mult(x,y):
#     return x*y
#
# a = mult(5,5)
# print(a)

#默认参数
#x*5
# def mult(x,y=5):
#     return x*y
#
# a = mult(7)
# print(a)

#可变对象：list dict set
#不可变对象：tuple int str float

#默认参数的陷阱
# def my_append(a,list1=[]):
#     list1.append(a)
#     return list1
#
# print(my_append('GaoYan'))
# print(my_append('ZhangYF'))

# def my_time(time=dt.datetime.now()):
#     tm.sleep(1)
#     print(time)
#
# my_time()
# my_time()
# my_time()

#None不可变对象
# def my_append(a,list1=None):
#     if list1 is None:
#         list1=[]
#
#     list1.append(a)
#     return list1
#
# print(my_append('GaoYan'))
# print(my_append('ZhangYF'))

# def my_time(time=None):
#     if time is None:
#         time = dt.datetime.now()
#     tm.sleep(1)
#     print(time)
#
# my_time()
# my_time()
# my_time()

#可变参数
#TODO 默认参数和可变参数混用

# def get_num(str,*list1):
#     sum = 0
#     for i in list1:
#         sum += i
#         print(str)
#     return sum
#
# print(get_num('ZYF',2,4,5))

#关键字参数
# def my_foo(**info):
#     print(info)
#
# my_foo(name='GaoYan',age='25',weight='90')

#多返回值
# def calc(x,y):
#     a = x*y
#     b = x+y
#     return a,b
#
# m,n = calc(5,3)
# print(m,n)

#结束函数
# def my_foo():
#     for i in range(100):
#         print(i)
#         if i == 50:
#             return i
#
# my_foo()

# 全局变量和局部变量
# def my_foo():
#     # name = 'GaoYan'
#     global name
#     name = 'GaoYan'
#     print(name)
#
# name = 'ZYF'
# my_foo()
# print(name)

#Ending
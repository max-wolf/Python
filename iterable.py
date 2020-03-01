# -*- coding:utf-8 -*-

from collections.abc import Iterable
from collections.abc import Iterator

# 并行迭代
# name = ['GaoYan','ZYF','Bob','Alice']
# score = [90, 80, 69, 79]
# weight = [90, 110, 100, 120]
#
# # for i in range(len(name)):
# #     print('name:{},score:{}'.format(name[i],score[i]))
# # zip
# # zip(name,score) --> [('GaoYan',90),('ZYF',80),('Bob',69),('Alice',79)]
# for a,b,c in zip(name,score,weight):
#     print('name:{},score:{},weight:{}'.format(a, b, c))

# 索引迭代
# name = ['GaoYan','ZYF','Bob','Alice']
# for i,j in enumerate(name):
#     print('index:{},name:{}'.format(i,j))

# 如何判断一个对象是否可迭代
# l = [2,3,4]
# l2 = [2,3,4]
# l3 = zip(l,l2)
# a = isinstance(l3,Iterable)
# print(a)

# 迭代器：所有可迭代的对象都可以转成迭代器
# for语句是语法糖，把可迭代的对象转成迭代器
# name = ['GaoYan','ZYF','Bob','Alice']
# for i in name:
#     print(i)
# it = iter(name) #转成迭代器
# while True:
#     try:
#         a = next(it)
#         print(a)
#     except StopIteration:
#         break

#迭代器也是可迭代的
# name = ['GaoYan','ZYF','Bob','Alice']
# it = iter(name)
# for i in it:
#     print(i)
# for i in it:
#     print(i)

# 可迭代的对象包含__iter__()
# 迭代器包含__iter__()和__next__()
# name = ['GaoYan','ZYF','Bob','Alice']
# a = isinstance(name, Iterator)
# print(a)
# it = iter(name)
# b = isinstance(it, Iterator)
# print(b)
# print(dir(name))
# print(dir(it))

# class Fib:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
# fib = Fib()
# for i,v in enumerate(fib):
#     if i == 5:
#         print(v)
#         break

#迭代器的计算是惰性的

for i in open('aaa.txt'):
    print(i)
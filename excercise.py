# -*- coding:utf-8 -*-

# import re

#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# qwer43 oiu3* $3
#alpha = [0,1,2,3,7,8,9]
#space = [6,10]

# def count_sth(strs):
#     a = []
#     b = []
#     c = []
#     d = []
#     i = 0
#     for ch in strs:
#         if ch.isalpha():
#             a.append(i)
#         elif ch.isspace():
#             b.append(i)
#         elif ch.isnumeric():
#             c.append(i)
#         else:
#             d.append(i)
#         i += 1
#     print('-----------')
#     print('alpha:', a)
#     print('space:', b)
#     print('numeric:', c)
#     print('other:', d)
#     print('-----------')
#
# for i in range(3):
#     strs_input = str(input('please input:'))
#     count_sth(strs_input)



#字符串反转
#qwerty --> ytrewq
#012345     543210

# def inverse_str(strs):
#     a=len(strs)-1
#     str_inverse = ''
#     while a>=0:
#         str_inverse=''.join([str_inverse,strs[a]])
#         a-=1
#     print(str_inverse)
#
# for i in range(3):
#     strs = str(input('please input:'))
#     inverse_str(strs)

#2,3
# #222=2*1+2*10+2*100
# def a_num(a):
#     res = 1
#     for i in range(1,a+1):
#         res *= i
#     return res
#
# def a_add(a):
#     sum = 0
#     l = []
#     for i in range(1,a+1):
#         tmp = a_num(i)
#         l.append(tmp)
#         sum += tmp
#     return sum, l
#
# print(a_add(20))

#100 50 25
#100+50*2+25*2
# def calc(height,counter):
#     sum = 0
#     res_height = height
#     for i in range(counter):
#         sum += res_height
#         res_height = res_height/2
#     return sum,res_height
#
# print(calc(100,3))


# 题目：求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
# 共有5个数相加)，几个数相加有键盘控制。
# a = 2  b = 5
# 222= 2*100 + 2*10 + 2*1
#   = 2*10^2 + 2*10^1 + 2*10^0
# 2+22+222+2222+22222
# a_add(2,1)+a_add(2,2)+a_add(2,3)...+a_add(2,5)
# def a_num(a,b):
#     sum = 0
#     for i in range(b):
#         tmp = a*pow(10,i)
#         sum += tmp
#     return sum
#
# def a_add(a,b):
#     res = 0
#     l = []
#     for i in range(b):
#         # i=0,1,2,3,4
#         # a_num(a,m):m=1,2,3,4,5
#         tmp = a_num(a,i+1)
#         l.append(tmp)
#         res += tmp
#     return l,res

# print(a_add(2,5))
# [2,22,222] 246
# l,res = a_add(2,5)
# print(l)
# print(res)

# 题目 求1+2!+3!+…+20!的和。
# 求阶乘 3!=1*2*3
# def a_num(a):
#     sum = 1
#     for i in range(1,a+1):
#         sum *= i
#     return sum
#
# # 求和
# def a_add(a):
#     res = 0
#     l = []
#     for i in range(1,a+1):
#         tmp = a_num(i) #嵌套函数
#         l.append(tmp)
#         res += tmp
#     return l,res
#
# #1+2+6
# print(a_add(20))

# 一球从m米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 100+50*2
# m+m/2*2+m/4*2+m/8*2
# m+m+m/2+m/4
# m=100,n=1
# def ball(m,n): # m是初始高度，n是落地次数
#     sum = 0
#     height = m
#     for i in range(n):
#         sum += height
#         height = m/pow(2,i)
#     return sum,height/2
#
# print(ball(100,1))
# print(ball(100,2))
# print(ball(100,3))
# print(ball(100,4))

#设计一个函数，可以接受任意数量参数，并计算参数之和/差/商/积
# 6,3,2
# 11,1,1,36

# def calc(*k):
#     sum = 0
#     sub = 0
#     sub2 = k[0]
#     div = k[0]
#     mul = 1
#     for x in k:
#         sum += x
#         mul *= x
#     for i,x in enumerate(k):
#         if i>0:
#             x = -x
#         sub += x
#     for x in k[1:]:
#         sub2 -= x
#         div /= x
#     print('sum:',sum)
#     print('sub:',sub2)
#     print('div:',div)
#     print('mul:',mul)
#
# calc(6,3,2)


#数组去重，保持元素相对位置不变
# [1,1,4,7,4,3,8,1] --> [1,4,7,3,8]
# def fun(*k):
#     l = []
#     for i in k:
#         # if i not in l:
#         #     l.append(i)
#
#         # if i in l:
#         #     continue
#         # l.append(i)
#
#         if i in l:
#             pass
#         else:
#             l.append(i)
#     return l
#
# def fun2(*k):
#     s = set(k)
#     l = list(s)
#     l.sort(key=k.index)
#     return l
#
# print(fun2(1,1,4,7,4,3,8,1))


# 斐波那契数列 0 1 1 2 3 5 8 13
#             a b
#               a b
# 递归实现
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# fib(6)=fib(5)+fib(4)=fib(4)+fib(3)+fib(3)+fib(2)=......
# 递推实现（循环）
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a,b = b, a+b
#     return a
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))

# [1,4,5,7,8,6] --> [7,12,12]
# [1,4,5,9,7,8,6] --> [7,12,12,9]
# [1,4,5,9]
# [6,8,7,0]
# def fun(*k):
#     l = list(k[:])
#     res = []
#     length = len(l)
#     if length%2 != 0:
#         l.insert(length//2+1, 0)
#     half_len = len(l)//2
#     l1 = l[:half_len]
#     l2 = l[-1:half_len-1:-1]
#     for a,b in zip(l1,l2):
#         res.append(a+b)
#     return res
#
# print(fun(1,4,5,9,7,8,6))

# 给定任意字符串，判断是否是手机号，如果是手机号，返回掩码后的手机号；如果不是手机号，返回false
# 13823450987 -> 138****0987
# def foo(phone:'str'):
#     if len(phone) != 11:
#         return False
#     if phone[0] != '1':
#         return False
#     if phone[:2] == '11' or phone[:2] == '12':
#         return False
#     l = [] # '0','1','2',...
#     for i in range(10):
#         l.append(str(i))
#     for i in phone:
#         if i not in l:
#             return False
#     return phone[:3] + '****' + phone[7:]

# 正则表达式
# def foo(phone):
#     if len(phone) != 11:
#         return False
#     res = re.match(r"1([3456789])\d{9}",phone)
#     if res != None:
#         return True
#     else:
#         return False
#
# print(foo('13823450987'))
# print(foo('11823450987'))
# print(foo('12823450987'))
# print(foo('138234509877'))
# print(foo('03823450987'))
# print(foo('13823u50987'))
# print(foo('1382350987'))

# 一群学生，有姓名、学号、成绩、年龄信息，分别从不同维度进行排序
# class Student:
#     def __init__(self, name, stuNo, score, age):
#         self.__name__ = name
#         self.__stuNo__ = stuNo
#         self.__score__ = score
#         self.__age__ = age
#
#     def get_name(self):
#         return self.__name__
#
#     def get_stuNo(self):
#         return self.__stuNo__
#
#     def get_score(self):
#         return self.__score__
#
#     def get_age(self):
#         return self.__age__
#
#     # 重写类的打印方法
#     def __str__(self):
#         return f"name:{self.get_name()} stuNo:{self.get_stuNo()} score:{self.get_score()} age:{self.get_age()}"
#
# s1 = Student('GaoYan', '133452', '90', '26')
# s2 = Student('ZhangYF', '133453', '80', '26')
# s3 = Student('Bob', '133443', '90', '24')
# s4 = Student('Alice', '133450', '70', '28')
# l = []
# l.append(s1)
# l.append(s2)
# l.append(s3)
# l.append(s4)
# # 对姓名排序
# res = sorted(l, key=lambda student:student.get_name())
# for i in res:
#     print(i)
# print('*******************')
# # 对成绩排序
# res = sorted(l, key=lambda student:(student.get_score(),student.get_age()))
# for i in res:
#     print(i)
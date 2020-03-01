# -*- coding:utf-8 -*-

# l = [23,64,87,84,  8,  1,  31, 3,  90, 77]
#     0  1  2  3   4   5   6   7    8   9
#   -10 -9 -8 -7   -6 -5   -4  -3  -2   -1
# print(l[5])
# print(l[-5])

# print(l[1:4])
# print(l[9:1:2])
# print(l[9:-5:-1])
# l2 = l[9:-5:-1][2:4]
# print(l2)
#
# t = (0,1,23,5)
# print(t[0:2])
# s = 'asdfqpweoi'
# print(s[:5])
# s2 = s[:]
# print(s2)
# l3 = l.copy()
# print(l3)

# [:] copy 都是浅拷贝：复制嵌套元素的引用
# a = ['GaoYan','ZhangYF',[90,110]]
# b = a[:]
# # b=['GaoYan','ZhangYF',[90,110]]
# print('b',b)
# b[0] = 'Alice'
# print('b',b)
# print('a',a)
# b[2][0] = 100
# print('b',b)
# print('a',a)

# l = [23,64,87,84,  8,  1,  31, 3,  90, 77]
# #插入元素
# # l[2:2]=['Gaoyan','zyf']
# # l[2]=['Gaoyan','zyf']
# #替换元素
# l[2:4]=['Gaoyan','zyf']
# print(l)

#实现strip
s='  qwer 31ewu       '
# print(s.strip())

def my_strip(s):
    while s[0]==' ':
        s = s[1:]
    while s[-1]==' ':
        s = s[:-2]
    return s

print(my_strip(s))
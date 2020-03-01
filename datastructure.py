# -*- coding:utf-8 -*-

#list
# list1 = [22,10,34]
# list2 = [12,87,9]
########  0  1  2  3
        #[22,90,10,34]
# list1.append(90)
# list1.insert(1,90)
#[22,10,34,12,87,9]

#访问元素
# list1.append(list2)
# print(list1[3][1])

#合并数组
# list1.extend(list2)
# print(list1)
# list3 = list1 + list2
# print('list1:',list1)
# print('list3:',list3)

#插入数组
# list1 = [22,10,34]
# list2 = [12,87,9]
# # [22,12,87,9,10,34]
# list4 = list1[:1] + list2 + list1[1:]
# print(list4)

#删除元素
# list1 = [34,43,17,22,34,43,17,99,34,43,17,22,10,34,43,17]
# list1.pop(2)
# del list1[2]
# for i in list1:
#     if i == 34:
#         list1.remove(34)
# print(list1)

# list1 = [34,43,17,22,34,43,17,99,34,43,17,22,10,34,43,17]
# print(len(list1))
# print(list1.count(34))
# print(100 in list1)

#输入指定值，存在即删除，不存在提示
# list1 = [34,43,17,22,34,43,17,99,34,43,17,22,10,34,43,17]
# a = 0
# while a < 3:
#     a += 1
#     input_num = int(input('please input number to delete:'))
#     if input_num in list1:
#         list1.remove(input_num)
#         print('%d is deleted '%(input_num))
#         print(list1)
#     else:
#         print('%d is not found '%(input_num))
#         print(list1)

#排序
# list1 = [34,43,17,22,34,43,17,99,34,43,17,22,10,34,43,17]
# list1.sort()
# list1.sort(reverse=True)
# list2 = sorted(list1, reverse=True)
# print(list2)

#tuple
# tuple1 = (21,76,90)
# print(len(tuple1))

# #list 和 tuple
# list1 = [('Alice',25),('Bob',67),('GaoYan',90),('Zhangyuanfei',59),('ZaoSen',50)]
#
# # def my_strategy(x):
# #     return x[0]
#
# # list2 = sorted(list1, key=my_strategy)
# #匿名函数
# list2 = sorted(list1, key=lambda x:len(x[0]), reverse=True)
# print(list2)

#dict
# dict1 = {'Alice':25,'Bob':67,'Gaoyan':90,'Zhangyuanfei':59,'Baosen':50}
#           key value
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# dict1['Kate']=88
# print(dict1)
# dict1.pop('Bob')
# print(dict1)
# list1 = sorted(dict1.items(),key=lambda x:x[1])
# print(list1)
# dict1 = {
#     'GaoYan':{
#         'Score':90,
#         'Height':160,
#         'Weight':90,
#         'Fruits':['banana','WaterLemon']
#     },
#     'Zhangyuanfei':{
#         'Score':59,
#         'Height':160,
#         'Weight':90
#     },
#     'Bob':{
#         'Score':34,
#         'Height':160,
#         'Weight':90
#     }
# }
# # dict1['GaoYan']['Fruits'].pop(1)
# # del dict1['Zhangyuanfei']
# list1 = sorted(dict1.items(),key=lambda x:x[1]['Score'])
# print(list1)

# #set
# list1 = [34,43,17,22,34,43,17,99,34,43,17,22,10,34,43,17]
# list2 = [34,324,17,22,34,7854,17,99,34,43,17,22,100,34,43,17]
# set1 = set(list1)
# set2 = set(list2)
# # set1.add(88)
# # set1.remove(10)
# print(set1&set2)
# print(set1|set2)

#Ending
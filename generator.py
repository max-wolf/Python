# range
# a = range(100,10,-8)
# b = list(a)
#
# for i in range(len(b)):
#     print(i,b[i])

# 列表生成式
# a = [i*3 for i in range(10) if i%2==0]
# print(a)

# 全排列
# a = ['A','B','C']
# b = ['X','Y','Z']
# # c = [i+j for i in a for j in b]
# c = [i+j for i,j in zip(a,b)]
# print(c)

# 遍历字典
# d = {'GaoYan':26,'ZhangYF':26, 'Bob':30}
# c = [key+'='+str(val) for key,val in d.items()]
# print(c)

# 把一个数组里大于10的元素筛选出来
# a = [3,65,8,71,11,0,5]
# b = [i for i in a if i>10]
# print(b)

# 取出数组中的字符串并转小写 lower() upper()
# a = ['GaoYan',834,'ZhangYF','Alice',99]
# b = [i.lower() for i in a if isinstance(i,str)]
# c = [i for i in a if isinstance(i,int)]
# print(c)

# 生成器表达式
# a = [i for i in range(20) if i%2==0]
# print(type(a))
# print('a:{}'.format(a))
# b = (i for i in range(20) if i%2==0)
# print(type(b))
# print('b:{}'.format(b))
# for i in b:
#     print(i)
# 生成器是一种迭代器

# 生成器
# yield
# def foo():
#     print('1')
#     yield 2 # return 2
#     print('3')
#     yield 4
#     print('5')
#     yield 6
#
# f = foo()
# print(next(f))
# print('********')
# print(next(f))
# print('********')
# print(next(f))
# for i in f:
#     print(i)

# 斐波那契数列 0 1 1 2 3 5 8 13
def fib(m):
    n,a,b = 0,0,1
    while n<m:
        a,b = b, a+b
    #   1,1
    #   1,2
    #   2,3
        n += 1
        yield a
    # return a

f = fib(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

# for i in fib(6):
#     print(i)
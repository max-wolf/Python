# 引入模块
# import module1
#
# print(dir(module1))
# module1.foo()

# 模块简写
# import module1 as m
#
# m.foo()


# 引入包
# import mypkg.module1 as m1
# import mypkg.module2 as m2
#
# m1.foo()
# m2.foo()

# from mypkg import module1 as m1
#
# m1.foo()

# 需要在__init__.py定义__all__变量
# from mypkg import *
#
# module1.foo()
# module2.foo()
# module1.hello()
# print(module1.name)

# 带参数运行
# import sys
#
# def test():
#     args = sys.argv
#     print(args)
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# test()
# 异常
# try:
#     print('111111')
#     a = 10/5
#     print('222222')
# # except只有在捕获异常时才会执行
# except ZeroDivisionError as e:
#     print('333333')
#     print(e)
# # finally无论有没有捕获异常都会执行
# finally:
#     print('444444')

# 异常继承关系
# try:
#     print('111111')
#     a = 10/0
#     print('222222')
# # 如果父类捕获了该类型的异常，那么它的子类就不会捕获该异常
# except Exception as e:
#     print('555555')
#     print(e)
# # 这里不会执行
# except ZeroDivisionError as e:
#     print('333333')
#     print(e)
# finally:
#     print('444444')

# 调用栈
# 异常是从下往上抛：被调用的方法抛给调用的方法
# def a():
#     10/0
#
# def b():
#     a()
#
# def c():
#     b()
#
# c()

# 自定义异常和手动抛出异常
# 自定义异常类型为MyError，继承自Exception
class MyError(Exception):
    pass

def foo(number):
    if number == 0:
        # 手动抛异常
        raise MyError('自定义异常')
    a = 10/number
    return a

print(foo(0))
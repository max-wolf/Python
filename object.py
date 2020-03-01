# 面向对象

from types import MethodType

# person1 = {'name':'GaoYan','age':26,'height':160}
# person2 = {'name':'ZhangYF','age':26,'height':170}
#
# print(person1.get('name'))

# 类
# class Person:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def print_age(self):
#         # print('{} age is:{}'.format(self.name, self.age))
#         print('%s age is:%d'%(self.name,self.age))
#
#     def set_name(self, name):
#         if len(name) > 5:
#             print('name is too long')
#             return
#         self.name = name
#
#     def set_age(self, age):
#         if age < 1 or age > 200:
#             print('age is to big or small')
#             return
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         if self.age < 10:
#             return 'child'
#         elif self.age > 60:
#             return 'elder'
#         else:
#             return 'normal'

# 实例化对象: 类-->对象
# person1 = Person('GaoYan',80,160)
# person2 = Person('ZhangYF',26,160)

# person1.print_age()
# person2.print_age()

# print(person1)
# print(Person)

# setter getter函数
# person1.name = 'Bob'
# person1.age = 30
# person1.print_age()

# person1.set_name('Bobiutgogu')
# person1.set_age(-1)
# person1.print_age()

# print(person1.get_age())

# 继承
# Person是父类，Staff是子类
# class Staff(Person):
#     def __init__(self, staffno, name, age, height):
#         super().__init__(name, age, height)
#         self.staffno = staffno
#
#     def work(self):
#         print('get to work')
#
# staff1 = Staff('12349435', 'GaoYan', 26, 160)
# staff1.work()
# staff1.print_age()
#
# class Student(Person):
#     def __init__(self, stuno, name, age, height):
#         super().__init__(name, age, height)
#         self.stuno = stuno
#
#     def study(self):
#         print('get to study')
#
# stu1 = Student('67657856', 'GaoYan', 26, 160)
# stu1.study()

# 访问限制

# class Student:
#     def __init__(self, name):
#         self.__name = name   # python把__name改成了_Student__name
#
#     def get_name(self):
#         print('name is '+self.__name)
#
# s = Student('GaoYan')
# # s.get_name()
# # print(s._Student__name)
# s.__name = 'Bob'
# s.get_name()
# print(s.__name)
# print(s._Student__name)

# 多态
# class Animal:
#     def run(self):
#         print('Animal is running')
#
# class Dog(Animal):
#     # 子类重写（覆盖）父类的同名方法
#     def run(self):
#         print('Dog is running')
#
#     def foo(self):
#         print('Dog is foo')
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running')
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
# dog.run()
# print(isinstance(animal, Animal))
# print(isinstance(dog, Dog))
# print(isinstance(cat, Cat))
# print(isinstance(dog, Animal))
# print(isinstance(cat, Animal))

# def run_twice(a):
#     a.run()
#     # a.run()
#     a.foo()

# run_twice(animal)
# run_twice(dog)
# run_twice(cat)

# 鸭子类型：如果一个东西如果看起来像鸭子，跑起来像鸭子，那它就是鸭子
# class Car:
#     def run(self):
#         print('Car is running')
#
#     def foo(self):
#         print('Car is foo')
#
# car = Car()
# # run_twice(car)
# run_twice(dog)

# 实例属性 类属性
# class Student:
#     name = 'Student'
#
#     def __init__(self, name):
#         self.__name = name   # __name是实例属性
#
#     def get_name(self):
#         print('name is '+self.__name)
#
# s = Student('GaoYan')
# # s.get_name()
# # print(Student.name)
# # print(s.name)
# s.name = 'Bob'
# # print(s.name)
# # print(Student.name)
# del s.name
# print(s.name)

# 装饰器
# @property
# class Student:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property  # getter
#     def name(self):
#         return 'name is ' + self.__name
#
#     @name.setter # setter
#     def name(self, name):
#         self.__name = name
#
#
# s = Student('GaoYan')
# print(s.name)
# s.name = 'ZhangYF'
# print(s.name)

# 静态方法 类方法
# class Student:
#     name = 'GaoYan'
#     def __init__(self):
#         self.score = 90
#
#     # 静态方法
#     @staticmethod
#     def run():
#         print(Student.name + ' is running')
#
#     # 类方法
#     @classmethod
#     def foo(self):  # self不是对象，是类
#         print(self)
#         print(self.name)
#         self.run()
#
#     def foo2(self):
#         print(self)
#         print(self.score)
#         print(self.name)

# Student.run()
# c = Student()
# c.run()
# c.foo2()
# print(Student.name)
# Student.foo()


# 给对象添加属性
# class Student:
#     name = 'Bob'
#
#     def __init__(self, age):
#         self.age = age

# s = Student(26)
# s.name = 'GaoYan'
# print(s.name)
# print(s.age)

# 给对象添加方法
# def set_age(self, age):
#     self.age = age

# s = Student(26)
# print(dir(s))
# s.set_age = MethodType(set_age, s)
# s.set_age(24)
# print(s.age)
# print(dir(s))
# # print(dir(Student))
# c = Student(30)
# print(dir(c))

# 给类添加方法
# def set_age(self, age):
#     self.age = age
#
# c = Student(80)
# print(dir(c))
# Student.set_age = set_age
# s = Student(26)
# s.set_age(30)
# print(s.age)
# print(dir(s))

# 限制属性
# class Student:
#     __slots__ = ('name','age','score')
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# s = Student('GaoYan', 26)
# print(s.name)
# print(s.age)
# s.score = 90
# print(s.score)

# 多重继承
# class Animal(object):
# class Animal:
#     def live(self):
#         print('living')
#
# class Runnable:
#     def run(self):
#         print('running')
#
# class Flyable:
#     def fly(self):
#         print('flying')
#
# class Chicken(Animal, Runnable, Flyable):
#     pass
#
# c = Chicken()
# c.run()
# c.fly()
# c.live()
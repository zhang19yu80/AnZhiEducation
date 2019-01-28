import os
from config import config

s = config.Config().get('URL')
print(s)
print (os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)) + '\..')


# for i in f:
#     print(i)

# gen = (x for x in range(5))
# lt = list(gen)
# print(lt,type(lt))


# class A(object):
#     c_num = 0
#
#     def __init__(self):
#         self.i_num = 1
#         A.c_num += 1
#
#     def say(self):
#         print('OK')
#
# a = A()
# b = A()
# c = A()
# print(A.c_num)

# a.c_num = 2
# a.i_num = 3
# print(a.c_num)
# print(A.c_num)
# print(a.i_num)
# print(A.i_num)

# def outer_func():
#     loc_list = []
#     def inner_func(name):
#         loc_list.append(len(loc_list) + 1)
#         print('%s loc_list = %s'%(name, loc_list))
#     return inner_func
#
# clo_func_0 = outer_func()
#
# clo_func_0('ppp')
# clo_func_0('ppp')
# clo_func_0('ppp')

# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score =score
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self,value):
#         self.score = value
#
#
# student = Student('ZY',90)
# student.name = 'ZH'
# print(student.name)


# class A:
#     def say_hello(self):
#         print('CaLL A.say_hello()')
#
# class B(A):
#     def say_hello(self):
#         print('Call B.say_hello()')
#         super().say_hello()
#
# b =B()
# b.say_hello()

# class A(object):
#     name = 'Zhang Yu'
#     def __init__(self,age):
#         self.age = age
#
#     def your_name(self):
#         print('Your nane is %s,and age is %s'%(self.name,self.age))
#
# class B(A):
#     def my_age(self):
#         print('my age is',self.age)
#
# b = B('2')
# print(b.name)
# b.your_name()
# b.my_age()
# # a =A('19')
# # a.your_name()



# class Tool(object):
#   # 使用赋值语句，定义类属性，记录创建工具对象的总数
#   count = 0
#   def __init__(self, name):
#      self.name = name
#      # 针对类属性做一个计数+1
#      Tool.count += 1
# # 创建工具对象
# tool1 = Tool("斧头")
# tool2 = Tool("榔头")
# tool3 = Tool("铁锹")
# # 知道使用 Tool 类到底创建了多少个对象?
# print("现在创建了 %d 个工具" % Tool.count)

#
# class MusicPlayer(object):
#     instance = None
#     init_flag = False
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#
#         return cls.instance
#
#     def __init__(self):
#
#         if not MusicPlayer.init_flag:
#             print("初始化音乐播放器")
#
#             MusicPlayer.init_flag = True
#
# player1 = MusicPlayer()
# print(player1)
#
# player2 = MusicPlayer()
# print(player2)



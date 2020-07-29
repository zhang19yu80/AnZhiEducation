import unittest
from payment import Payment
from unittest import mock


class PaymentTest(unittest.TestCase):
    """
    测试支付接口
    """

    def setUp(self):
        self.payment = Payment()

    def test_success(self):
        """
        测试支付成功
        :return:
        """
        self.payment.authe = mock.Mock(return_value=200)
        res = self.payment.pay(user_id=10001, card_num="123444", amount=1000)
        self.assertEqual("success", res)

    def test_fail(self):
        """
        测试支付成功
        :return:
        """
        self.payment.authe = mock.Mock(return_value=500)
        res = self.payment.pay(user_id=10002, card_num="1233444", amount=1000)
        self.assertEqual("fail", res)

    def test_retry_success(self):
        """
                测试支付失败重试在成功
                side_effect 可以为序列类型 异常类型，对象
                如果为序列类型 每次调用mock对象，会依次将side effcet中的元素返回
                :return:
                """
        self.payment.authe = mock.Mock(side_effect=[TimeoutError, 200])
        res = self.payment.pay(user_id=10003, card_num="1234444", amount=1000)
        self.assertEqual("success", res)


if __name__ == '__main__':
    unittest.main()

# from unittest import mock
# import json


# class Connect_things(object):
#     def weixin(self):
#         pass
#
#     def xiaofeiji(self):
#         pass
#
# class Connect_things_Mock(object):
#
#     def weixin_mock(self):
#         Connect_things.weixin = mock.Mock(return_value={"aaa":"bbb","ccc":4})
#         return Connect_things.weixin()
#
#     def xiaofeiji_mock(self):
#         pass
#
#
# print(y:=Connect_things_Mock().weixin_mock(),type(y))
#
# # n = json.dumps(Connect_things_Mock().weixin_mock())
# print(n:=json.dumps(Connect_things_Mock().weixin_mock()),type(n))
#
# print(x:=json.loads(n),type(x))





# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')



# from shutil import copyfile
# import time
#
# start_time = time.time()
# source = 'C:\\smartacs\\images\\student\\3_1301班_俊俊1.jpg'
# for i in range(2,6001):
#     target = f'C:\\smartacs\\images\\student\\3_1301班_俊俊{i}.jpg'
#     copyfile(source,target)
# end_time = time.time()
# YS = end_time - start_time
# print(f'共耗时：{YS}')12

# print(os.path.join(BASE_PATH, 'data'))D
#
# class AuctionException(Exception): pass
# class AuctionTest:
#     def __init__(self, init_price):
#         self.init_price = init_price
#     def bid(self, bid_price):
#         d = 0.0
#         try:
#             d = float(bid_price)
#         except Exception as e:
#             # 此处只是简单地打印异常信息
#             print("转换出异常：", e)
#             # 再次引发自定义异常
#             raise AuctionException("竞拍价必须是数值，不能包含其他字符！")  # ①
#             raise AuctionException(e)
#         if self.init_price > d:
#             raise AuctionException("竞拍价比起拍价低，不允许竞拍！")
#         initPrice = d
# def main():
#     at = AuctionTest(20.4)
#     try:
#         at.bid("df")
#     except AuctionException as ae:
#         # 再次捕获到bid()方法中的异常，并对该异常进行处理
#         print('main函数捕捉的异常：', ae)
#
# main()

# def test(name,state_code=None):
#     if not state_code:
#         state_code = [200]
#         print(type(state_code))
#     print('My name is {0}, and the state is {1}'.format(name,state_code))
#
# #p = test('Zhang Yu')
# h = test('Zhang Yu',[400,500])



# from log.log import logger
# import sys, time
#
# def log(func):
#     def zsq(*args,**kwargs):
#         logger.info("开始 {0} - {1} 自动化测试".format(
#             sys._getframe().f_code.co_filename.split('\\')[-1],
#             sys._getframe().f_code.co_name))
#         func(*args,**kwargs)
#         logger.info('完成 {} - {}(1)'.format(
#             sys._getframe().f_code.co_filename.split('\\')[-1],
#             sys._getframe().f_code.co_name))
#     return zsq
#
# def timer(func):
#     def zsq(*args,**kwargs):
#         print('开始时间%s'%time.time())
#         time.sleep(3)
#         func(*args,**kwargs)
#         print('结束时间%s'%time.time())
#     return zsq
#
#
# @log
# def test1():
#     print('正在运行测试用例。')
#
# test1()

# def my_generator(n):
#     for i in range(n):
#         temp = yield
#         print(f'我是{temp}')
#
# g=my_generator(5)
#
# print(next(g)) #输出0
#
# print(next(g)) #输出1
#
# g.send(100) #本来输出2，但是传入新的值100，改为输出100
#
# print(next(g)) #输出3
#
# print(next(g)) #输出4

# his = im.histogram()
# values = {}
#
# for i in range(256):
#     values[i] = his[i]
#
# for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
#     print(j,k)

# def fn(var1, var2=[]):
#   var2.append(var1)
#   print(var2)

# def fn(var1, var2=None):
#   if not var2:
#     var2 =[]
#   var2.append(var1)
#   print(var2)
#
# def fn(var1):
#     var2 = []
#     var2.append(var1)
#     print(var2)
#
# fn(3)
# fn(4)
# fn(5)

# def get_old(list):
#     # res = []
#     for i in list:
#         if i % 2:
#             yield i
#     # return res
#
# def main():
#     lst = range(10)
#     for i in get_old(lst):
#         print(i)
#
#
# # main()
#
# res = (x for x in range(10))
# print(next(res))
# print(next(res))
# print(next(res))

#
# def function():
#     print(sys._getframe().f_code.co_filename)  # 当前位置所在的文件名
#     print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
#     print(sys._getframe().f_code.)  # 当前位置所在的行号



# class AAA(object):
#     s = 123
#     def BBB(self):
#         x = 456
#         self.y = 789
#
#
#
# d = AAA()
# d.y



# s = test123.get_somethings().get_jsessionid()
# print(s)

# p = general.Get_Somethings().get_jsessionid()
# print(p)
# print (os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)) + '\..')


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
#
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


# class A(object):
#     def say_hello(self):
#         print('CaLL A.say_hello()')
#
# class B(A):
#     def say_hello(self):
#         print('Call B.say_hello()')
#         super().say_hello()
#
# b =A()
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

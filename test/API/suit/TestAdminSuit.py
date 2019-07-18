import unittest, os
from config import config
from utils.mail import Email
from utils.HTMLTestRunner_PY3 import HTMLTestRunner



case_path = os.path.join(config.BASE_PATH, 'test', 'API','case') #测试用例位置

report = config.REPORT_PATH + '\\report.html' #测试报告位置

suit = unittest.defaultTestLoader.discover(case_path,pattern="Test*.py") #实例化测试套件

if __name__=='__main__':
    with open(report,'wb') as f:
        runner = HTMLTestRunner(stream=f,verbosity=2, title='安智智慧校园 API 自动化测试报告',description='3月22日2.0.1版本上线前最后一次自动化测试')
        runner.run(suit)
    e = Email(title='安智智慧校园 API 自动化测试报告',
              message='这次的测试报告，请查收！',
              receiver='28766012@qq.com',
              server='smtp.163.com',
              sender='zhang19yu80@163.com',
              password='8FangPing',
              path=report
              )
    e.send()

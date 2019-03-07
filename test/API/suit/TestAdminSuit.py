import unittest, os
from config import config
from utils.mail import Email
from utils.HTMLTestRunner_PY3 import HTMLTestRunner



case_path = os.path.join(config.BASE_PATH, 'test', 'API','case')

suite=unittest.defaultTestLoader.discover(case_path,pattern="Test*.py")

if __name__=='__main__':
    report = config.REPORT_PATH + '\\report.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='安智智慧校园自动化测试报告',description='这是一次 full-testing')
        runner=unittest.TextTestRunner()
        runner.run(suite)
    # e = Email(title='百度搜索测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='28766012@qq.com',
    #           server='smtp.163.com',
    #           sender='zhang19yu80@163.com',
    #           password='8FangPing',
    #           path=report
    #           )
    # e.send()

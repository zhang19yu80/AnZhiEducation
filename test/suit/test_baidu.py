# import os
import time
import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from config import config
from log.log import logger
from utils.file_reader.excel_reader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
from test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage

class TestBaiDu(unittest.TestCase):
    #URL = "http://www.baidu.com"
    URL = config.Config().get('URL')
    excel = config.DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuResultPage(browser_type='chrome').get(self.URL, maximize_window=False)
    def sub_tearDown(self):
        self.page.quit()

    # def test_search_0(self):
    #     self.driver.find_element(*self.locator_kw).send_keys('selenium 灰蓝')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    report = config.REPORT_PATH + '\\report.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='易泊充自动化测试报告',description='这是一次 full-testing')
        runner.run(TestBaiDu('test_search'))
    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='601875688@qq.com',
              server='smtp.163.com',
              sender='zhang19yu80@163.com',
              password='8FangPing',
              path=report
              )
    e.send()
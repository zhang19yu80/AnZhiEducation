from test.API.API_common import general
from log.log import logger
import unittest, requests,time, sys

class TestAdmin(unittest.TestCase):
    URL_platform = general.url + general.sub_url[1]
    header = general.header

    @classmethod
    def setUpClass(cls):
        # general.Get_Somethings().login_admin()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_mian(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        login_url = 'https://testadmin.xiaopay.net/main.html'
        response = requests.get(login_url,headers=self.header)
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        logger.info('完成 {} - {}(1),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_platform(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"agentid":"","description":"","fun":4,"nameorphone":"","pageindex":1,"pagesize":10}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json['ack'], '0', "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(2),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))


    def test_platform_addaccount(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"fun":0,"username":"自动化测试","phone":"18812341234","description":"自动化测试自动化测试自动化测试","roles":31,"ismanage":0}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], ['0','69'], "Fail-没有添加成功")
        logger.info('完成 {} - {}(3),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_platform_editaccount(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"agentid":"","description":"","fun":4,"nameorphone":"","pageindex":1,"pagesize":10}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        results = response.json()['results'] #得到添加的管理员列表
        id = [i['id'] for i in results if i['phone'] == "18812341234"] #得到 id 列表
        data = {"id":id,"fun": 3, "username": "自动化测试-编辑后", "phone": "18812341234", "description": "自动化测试自动化测试自动化测试", "roles": 31,
                "ismanage": 0}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json['ack'], '0', "Fail-没有编辑成功")
        logger.info('完成 {} - {}(4),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))



if __name__ == '__mian__':
    unittest.main()
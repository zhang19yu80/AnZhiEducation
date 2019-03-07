from test.API.API_common import general
from log.log import logger
import unittest, requests, time, sys

class TestAdmin(unittest.TestCase):
    header = general.header

    @classmethod
    def setUpClass(cls):
        # general.Get_Somethings().login_admin()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_OperationType(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_agent = general.url + '/youbay/svbasicdata/Common'
        data = {"fun":83}
        response = requests.post(url=URL_agent, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json['ack'], '0', "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(1),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_OperationTypeList(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_school = general.url + '/youbay/svpc/QuerylWechatPushTypeList'
        data = {}
        response = requests.post(url=URL_school, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json['ack'], '0', "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(2),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_SendUserDetailList(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_school = general.url + '/youbay/svpc/QuerylSenduserdetailList'
        data = {"senddate":"20190301", "pageindex":1, "pagesize":10}
        response = requests.post(url=URL_school, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'],['0','131'], "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(3),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_AgentList(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_agent = general.url + '/youbay/svbasicdata/Common'
        data = {"fun":7}
        response = requests.post(url=URL_agent, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json['ack'], '0', "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(4),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_PushLogDaily(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_agent = general.url + '/youbay/svpc/QuerylPushlogdaily'
        data = {"startdate":"20190300","enddate":"20190300"}
        response = requests.post(url=URL_agent, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], ['0','66','131'], "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(5),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))


if __name__ == '__mian__':
    unittest.main()
from test.API.API_common import general
from log.log import logger
import unittest, requests, time

class TestAdmin(unittest.TestCase):
    header = general.header

    @classmethod
    def setUpClass(cls):
        general.Get_Somethings().login_admin()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_SearchAgent(self):
        URL_agent = general.url + '/youbay/svbasicdata/Agent'
        data = {"fun":4}
        response = requests.post(url=URL_agent, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json['ack'], '0', "Fail-没有成功获得数据")
        logger.info('完成 TestAdmin_PlatformVerify - test_SearchAgent(1),状态码: %s'%response.status_code)

    def test_SearchSchoolWait(self):
        URL_school = general.url + '/youbay/svbasicdata/School'
        data = {"fun":10, "pageindex":1, "pagesize":10, "state":1}
        response = requests.post(url=URL_school, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], ['0','66'], "Fail-没有成功获得数据")
        logger.info('完成 TestAdmin_PlatformVerify - test_SearchSchool(2),状态码: %s'%response.status_code)

    def test_SearchSchoolPassed(self):
        URL_school = general.url + '/youbay/svbasicdata/School'
        data = {"fun":12, "pageindex":1, "pagesize":10}
        response = requests.post(url=URL_school, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], ['0','66'], "Fail-没有成功获得数据")
        logger.info('完成 TestAdmin_PlatformVerify - test_SearchSchoolPassed(3),状态码: %s'%response.status_code)

    def test_SearchSchoolRejected(self):
        URL_school = general.url + '/youbay/svbasicdata/School'
        data = {"fun":10, "pageindex":1, "pagesize":10, "state":3}
        response = requests.post(url=URL_school, headers=self.header, data=data)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], ['0','66'], "Fail-没有成功获得数据")
        logger.info('完成 TestAdmin_PlatformVerify - test_SearchSchoolRejected(4),状态码: %s'%response.status_code)


if __name__ == '__mian__':
    unittest.main()
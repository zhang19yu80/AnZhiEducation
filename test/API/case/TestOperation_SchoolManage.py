from test.API.API_common import general
from log.log import logger
import unittest, requests, time, sys

class TestAdmin(unittest.TestCase):
    header = general.header

    @classmethod
    def setUpClass(cls):
        # general.Get_OperationSomethings().login_Operation()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_AddAgent(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_agent = general.url_operate + general.sub_url[2]
        data = {"isagency":0, "sortinx":0, "description":"自动化测试自动化测试自动化测试",
                "provinceid":"20", "cityid":"181", "districtid":"1799", "contacts":"鱼鱼风",
                "wechatnumber":"testnumberone", "phonenumber":"18878907890", "parentid":1,
                "fun":0, "agentname":"自动化机构"}
        response = requests.post(url=URL_agent, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json['ack'], '0', "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(1),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))
        time.sleep(1)




if __name__ == '__mian__':
    unittest.main()
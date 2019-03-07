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


    def test_SearchCard(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_card = general.url_operate + '/pages/cardcenter/school-card-data-sta.html'
        response = requests.get(url=URL_card, headers=self.header)
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        logger.info('完成 {} - {}(1),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))



if __name__ == '__mian__':
    unittest.main()
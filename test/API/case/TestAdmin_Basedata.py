from test.API.API_common import general
from log.log import logger
from config.config import Config
import unittest, requests, time, sys

class TestAdmin(unittest.TestCase):
    URL_platform = general.url + general.sub_url[1]
    header = general.header

    @classmethod
    def setUpClass(cls):
        general.Get_Somethings().login_admin()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_WechatManage(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"wechattype":"","wechatname":"","fun":24,"settingtype":"","pageindex":1,"pagesize":10}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertIn(res_json['ack'],['0','66'],"Fail-没有成功获得数据")
        logger.info('完成 {} - {}(1),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name,response.status_code))

    def test_AddWechatManage(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"wechattype":0,"wechatname":"自动化公众号","wechatcode":"gh_1a4d7bb4fb6b",
                "settingtype":0,"regdate":"20190220","fun":20,"channeltype":"2",
                "appsecret":"e0c9be703373144ad15c8239a794f9b5","appid":"wx366651f06fadab1c"}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertIn(res_json['ack'],['0','69'],"Fail-没有添加成功")
        logger.info('完成 {} - {}(2),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_WechatMenuConfig(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_wechat = Config().get('AdminURL') + '/youbay/svpc/QueryWechatMenu'
        data = {"appid":"wx366651f06fadab1c"}
        response = requests.post(URL_wechat, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertEqual(res_json['ack'],'0',"Fail-没有获得数据")
        logger.info('完成 {} - {}(3),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_WechatTemplateList(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        URL_wechatTL = Config().get('AdminURL') + '/youbay/svpc/QuerylWechatPushTempLateList'
        data = {"appid":"wx366651f06fadab1c","pageindex":"1","pagesize":"10"}
        response = requests.post(URL_wechatTL, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertEqual(res_json['ack'],'0',"Fail-没有获得数据")
        logger.info('完成 {} - {}(4),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_EditWechatManage(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"wechattype": 0, "wechatname": "自动化公众号", "wechatcode": "gh_1a4d7bb4fb6b",
                "settingtype": 0, "regdate": "20190220", "fun": 20, "channeltype": "2",
                "appsecret": "e0c9be703373144ad15c8239a794f9b5", "appid": "wx366651f06fadab1c"}
        requests.post(self.URL_platform, data=data, headers=self.header)
        time.sleep(1)
        newdata = {"fun": 22,"id":1}
        response = requests.post(self.URL_platform, data=newdata, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], '0', "Fail-没有添加成功")
        logger.info('完成 {} - {}(5),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_WechatCommercialTenantManage(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"wechattype":"","wechatname":"","fun":34,"settingtype":"","pageindex":1,"pagesize":10}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertIn(res_json['ack'],['0','66'],"Fail-没有成功获得数据")
        logger.info('完成 {} - {}(6),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_AddWechatCommercialTenantManage(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"mchid":"123123","mchname":"自动化商户号","fun":30,
                "mchtype":0,"mchvest":0,"status":1, "payappid":"23432sdfsr",
                "payappsert":"dfds324324","paykey":"34dsfdsfdf",
                "terminalip":"127.0.0.1","vestid":1}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertIn(res_json['ack'],['0','69'],"Fail-没有成功获得数据")
        logger.info('完成 {} - {}(7),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_EditWechatCommercialTenantManage(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"agentid": "", "description": "", "fun": 34, "nameorphone": "", "pageindex": 1, "pagesize": 10}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        results = response.json()['results']  # 得到添加的管理员列表
        id = [i['id'] for i in results if i['paykey'] == "34dsfdsfdf"]  # 得到 id 列表
        time.sleep(1)
        newdata = {"mchid":"123123","mchname":"编辑自动化商户号","fun":33,
                "mchtype":0,"mchvest":0,"status":1, "payappid":"23432sdfsr",
                "payappsert":"dfds324324","paykey":"34dsfdsfdf",
                "terminalip":"127.0.0.1","vestid":1,"id":id}
        response = requests.post(self.URL_platform, data=newdata, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], ['0','66'], "Fail-没有添加成功")
        logger.info('完成 {} - {}(8),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))

    def test_DataDictMangage(self):
        logger.info("开始 {0} - {1} 自动化测试".format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name))
        data = {"dicname":"","dictype":"","fun":14,"pageindex":1,"pagesize":10}
        response = requests.post(self.URL_platform, data=data, headers=self.header)
        res_json = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertIn(res_json['ack'], '0', "Fail-没有添加成功")
        logger.info('完成 {} - {}(9),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, response.status_code))




if __name__ == '__mian__':
    unittest.main()
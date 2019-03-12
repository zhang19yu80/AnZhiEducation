from test.API.API_common import general
from log.log import logger
import unittest, requests, time, sys, json

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
        #创建运营机构
        URL_agent = general.url_operate + general.sub_url[4]
        data = {"isagency":0, "sortinx":0, "description":"自动化测试自动化测试自动化测试",
                "provinceid":"20", "cityid":"181", "districtid":"1799", "contacts":"鱼鱼风",
                "wechatnumber":"testnumberone", "phonenumber":"18878907890", "parentid":1,
                "fun":0, "agentname":"自动化机构"}
        requests.post(url=URL_agent, data=data, headers=self.header)
        logger.info("完成机构创建")
        time.sleep(1)
        #查询运营机构
        data1 = {"fun":4}
        resopnse = requests.post(url=URL_agent, data=data1, headers=self.header)
        res_json = resopnse.json()
        institutionsid = res_json.get('results')[0].get('children')[0].get('id')
        logger.info("获得机构ID")
        time.sleep(1)

        #创建学校
        URL_agent1 = general.url_operate + general.sub_url[3]
        data1 = {"fun":22, "schoolname":"自动化学校", "teachingstage":"1|2|3|4|5",
                "schooltype":1, "cityid":"181", "district":"1799", "regionaltypes":1,
                "provinceid":"20", "adminphone":"18890909090", "adminname":"自动人",
                "institutionsid":institutionsid, "channeltype":1, "smspush":1, "synopen":0,
                "configlist":'''[{"funpid": 1,"funid": 2,"funvalue":"1"},{"funpid": 3,"funid": 4,"funvalue":"4"}]''',
                "photolist":'''[{"photourl":" https://youbay2017.oss-cn-hangzhou.aliyuncs.com/awsp/web/image/20190308/93b03d3d8209dd79eb10ce1edd84748a.jpg"}]''',
                "orderid":0, "schoolid":0}
        resopnse1 = requests.post(url=URL_agent1, data=data1, headers=self.header)
        tmpid = resopnse1.json().get('results').get('id')
        logger.info("完成学校创建并获得学校ID")
        time.sleep(1)

        #审批学校
        data2 = {"fun": 31, "orderid":tmpid, "state":2,"wechatid":1}
        resopnse2 = requests.post(url=URL_agent1, data=data2, headers=self.header)
        schoolid = resopnse2.json().get('results').get('schoolid')
        logger.info("学校通过审批")
        time.sleep(1)

        #创建运营人员
        data3 = {"fun":10, "username":"自动化测试", "phone":"18809090909",
                 "description":"自动化测试自动化测试自动化测试", "operatorroles":32,
                 "inschoolroles":33, "ismanage":0, "agentid":institutionsid,
                 "rolelimits":3, "userschools":schoolid}
        resopnse3 = requests.post(url=URL_agent, data=data3, headers=self.header)
        res_json1 = resopnse2.json()
        self.assertEqual(resopnse3.status_code, 200, "Fail-此API不通！")
        self.assertEqual(res_json1['ack'], '0', "Fail-没有成功获得数据")
        logger.info('完成 {} - {}(1),状态码: {}'.format(
            sys._getframe().f_code.co_filename.split('\\')[-1],
            sys._getframe().f_code.co_name, resopnse2.status_code))

if __name__ == '__mian__':
    unittest.main()
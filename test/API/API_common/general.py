import requests,time, pytesseract
from config import config
#from PIL import Image

url = config.Config().get('AdminURL')
url_operate = config.Config().get('OperationURL')
sub_url = ['/youbay/svbasicdata/Login',
           '/youbay/svbasicdata/Platform',
           '/youbay/svbasicdata/Common',
           '/youbay/svbasicdata/School',
           '/youbay/svbasicdata/Agent']

header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
          "Access-Control-Allow-Credentials": "true",
          "Access-Control-Allow-Headers": "X-Requested-With,content-type",
          "Access-Control-Allow-Methods": "POST, GET, OPTIONS, PUT, DELETE",
          "Access-Control-Allow-Origin": "https://testadmin.xiaopay.net",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
          }

class Get_Somethings(object):
    _my_url = url + sub_url[0]

    def __init__(self, tel='13888888888', pwd='e14fb1b2db5862755bae8c48d29856ee'):
        self.tel = tel
        self.pwd = pwd
        self.fun = 5
        self.checkcodetype = 2

    def _get_sessionid(self):
        '''
        You can get the sessionid using this function.
        :return: a sessionid.
        '''
        data = {"fun": 2}
        response = requests.post(url=self._my_url, data=data, headers=header)
        sessionid = response.cookies['rtpc_scid']
        return "rtpc_scid=" + sessionid

    def _new_header(self):
        '''
        This function will update the header to add the sessionid.
        :return: None
        '''
        header["Cookie"] = self._get_sessionid()  #得到 sessionid
        return None

    # def _get_SMS(self):
    #     #     '''
    #     #     You got the SMS using this function.
    #     #     :return: a SMS.
    #     #     '''
    #     #     self._new_header() #更新加入 Cookie 信息的 header
    #     #     data = {'checkcodetype': self.checkcodetype, 'fun': self.fun, 'phone': self.tel, 'pwd': self.pwd}
    #     #     response = requests.post(url=self._my_url, data=data, headers=header) #发送验证码
    #     #     sms = response.json()['smscode']
    #     #     res_sms = sms[-4:] #得到短信验证码
    #     #     # time.sleep(0.5)
    #     #     # res_sms = Get_SMS_From_Web().get_SMS()
    #     #     return res_sms

    def login_admin(self):
        '''
        Mark the sessionid with login authentication, and keep to two hours.
        :return: None
        '''
        self._new_header()
        sms = "10248520"
        data = {"fun": 4, "phone": self.tel, "pwd": self.pwd, "smscode": sms, "logintype": "admin"}
        response = requests.post(url=self._my_url, data=data, headers=header)
        results = '登录成功 ^_^' if response.json()['ack'] == '0' else '登陆失败 -_-'
        return results

class Get_OperationSomethings(object):
    _my_url = url_operate + sub_url[0]

    def __init__(self, tel='13866666666', pwd='e14fb1b2db5862755bae8c48d29856ee'):
        self.tel = tel
        self.pwd = pwd
        self.fun = 1

    def _get_sessionid(self):
        '''
        You can get the sessionid using this function.
        :return: a sessionid.
        '''
        data = {"fun": 11}
        response = requests.post(url=self._my_url, data=data, headers=header)
        sessionid = response.cookies['rtpc_scid']
        return "rtpc_scid=" + sessionid

    def _new_header(self):
        '''
        This function will update the header to add the sessionid.
        :return: None
        '''
        header["Cookie"] = self._get_sessionid() #得到 sessionid
        return None


    def login_Operation(self):
        '''
        Mark the sessionid to pass the login authentication, and keep to two hours.
        :return: results
        '''
        self._new_header()
        data = {"fun": self.fun, "phone": self.tel, "pwd": self.pwd}
        response = requests.post(url=self._my_url, data=data, headers=header)
        results = '登录成功 ^_^' if response.json()['ack'] == '0' else '登陆失败 -_-'
        return results

# class Get_SMS_From_Web(object):
#     """
#     使用这个类的前提先运行 login_SMSWeb.login_SMSWeb() 确定已登录网站。
#     """
#     LB_URL = 'http://mos.wxchina.com/SmsMgr/SendTracking/LoadBatchs'
#     LP_URL = 'http://mos.wxchina.com/SmsMgr/SendTracking/LoadPhones'
#
#     sub_header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#                   "Connection": "keep-alive",
#                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
#                   "Cookie": "Cookie: ASP.NET_SessionId=fpd3t000gu5xa5k5jnslabta; UserSessionId=fpd3t000gu5xa5k5jnslabta; MenusBlockIDs=10000,10010,10011,10012,10013,10014,17000,12000,13000,14000,15000,18000,18200; .ASPXAUTH=E038085FA3B1CD92687DD0498D6C81246EFC505A1F74E7EB372649BB1E4FB200C4490C6581FDB861B827B83F81A562BCE22752A6D9EDC301D0B7F0B2F6C6D0BC24576391E209C3CEC8AB954930D659A27253B82AE8E067952C9F298701210F48BEA86BB77EFB1F1B6562A73205990B635F0F340F2C98FF65380EDC623D895D1142C8EC2B287ACB4EAD3269D55EA20170; ControllerName=sendtracking",
#                   }
#
#     def _get_ls_id(self):
#         # login_SMSWeb().login_SMSWeb()
#         data = {"PageIndex":1, "PageSize":10, "SortName":"id", "Sortorder":"asc",
#                 "BatchState":-1, "UserName":"kmhxt@kmhxt", "isShowchild":"true",
#                 "starttime":"2019-03-15 00:00:00", "endtime":"2019-03-15 23:59:59",
#                 "Msg_Type":1, "onTime":"true"}
#         response = requests.post(url=self.LB_URL, data=data, headers=self.sub_header)
#         res_json = response.json()
#         ls_cell = res_json.get('rows')
#         # ls_id = [x['id'] for x in ls_cell]
#         ls_id = []
#         for x in ls_cell:
#             ls_id.append(x['id'])
#         return ls_id
#
#     def get_SMS(self):
#         lst_id = self._get_ls_id()
#         for batchid in lst_id:
#             data = {"PageIndex": 1, "PageSize": 15, "SortName": "id", "Sortorder": "asc",
#                     "batchid": batchid, "type": 0}
#             response = requests.post(url=self.LP_URL, data=data, headers=self.sub_header)
#             print(response.json())
#             phone_number = response.json().get('rows')[0].get('id')
#             if phone_number == '13888888888':
#                 phone_SMS = response.json().get('rows')[0].get('cell').get('content')[6:12]
#                 return phone_SMS
#             else:
#                 pass



# class login_SMSWeb(object):
#     '''
#     登录发短信群发网站
#     '''
#     URL_cookie = 'http://mos.wxchina.com/PublicWindow/Public/Login?ReturnUrl=%2f'
#     URL_login = 'http://mos.wxchina.com/PublicWindow/Public/Login?ReturnUrl=%2F'
#     URL_img = 'http://mos.wxchina.com/PublicWindow/Public/ValidateCode?timestamp' + str(int(time.time()))
#     sub_header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#                   "Connection": "keep - alive",
#                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
#                  }
#     def _get_SessionId(self):
#         response = requests.get(url=self.URL_cookie, headers=self.sub_header)
#         sessionid = response.cookies["ASP.NET_SessionId"]
#         return "ASP.NET_SessionId=" + sessionid
#
#     def _new_header(self):
#         self.sub_header["Cookie"] = self._get_SessionId() #得到 sessionid
#         return None
#
#     def _get_Verifycode(self):
#         requests.get(url=self.URL_login, headers=self.sub_header)
#         time.sleep(0.5)
#         response1 = requests.get(self.URL_img)
#         with open('E:\AnZhiEducationTestFramework\data\\verifycode.png', 'wb') as f:
#             f.write(response1.content)
#         im = Image.open('E:\AnZhiEducationTestFramework\data\\verifycode.png')
#         verifycode = pytesseract.image_to_string(im)
#         return verifycode
#
#     def login_SMSWeb(self):
#         self._new_header()
#         print(self.sub_header)
#         while True:
#             verifycode = self._get_Verifycode()
#             print(verifycode)
#             data = {"UserName":"kmhxt@kmhxt", "Password":"vn8BB6w9", "validate":verifycode, "x":62, "y":17}
#             response1 = requests.post(url=self.URL_login, data=data, headers=self.sub_header)
#             print(response1.status_code,response1.text)
#             if response1.status_code == 302:
#                 break
#
#         else:
#             print('成功登录')



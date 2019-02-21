import requests
from config import config

url = config.Config().get('AdminURL')
sub_url = ['/youbay/svbasicdata/Login','/youbay/svbasicdata/Platform','/youbay/svpc/QueryWechatMenu','/youbay/svpc/QuerylWechatPushTempLateList']
header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
          "Access-Control-Allow-Credentials": "true",
          "Access-Control-Allow-Headers": "X-Requested-With,content-type",
          "Access-Control-Allow-Methods": "POST, GET, OPTIONS, PUT, DELETE",
          "Access-Control-Allow-Origin": "https://testadmin.xiaopay.net",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
          }

class Get_Somethings(object):
    my_url = url + sub_url[0]
    def __init__(self, tel='13888888888', pwd='e14fb1b2db5862755bae8c48d29856ee', fun=5, checkcodetype=2):
        self.tel = tel
        self.pwd = pwd
        self.fun = fun
        self.checkcodetype = checkcodetype

    def _get_sessionid(self):
        '''
        You can get the sessionid using this function.
        :return: a sessionid.
        '''
        data = {"fun": 2}
        response = requests.post(url=self.my_url, data=data, headers=header)
        sessionid = response.cookies['rtpc_scid']
        return "rtpc_scid=" + sessionid

    def _new_header(self):
        '''
        This function will update the header to add the sessionid.
        :return: None
        '''
        # global header
        header["Cookie"] = self._get_sessionid() #得到 sessionid
        return None

    def _get_SMS(self):
        '''
        You got the SMS using this function.
        :return: a SMS.
        '''
        self._new_header() #更新加入 Cookie 信息的 header
        data = {'checkcodetype': self.checkcodetype, 'fun': self.fun, 'phone': self.tel, 'pwd': self.pwd}
        response = requests.post(url=self.my_url, data=data, headers=header)
        sms = response.json()['smscode']
        res_sms = sms[-4:] #得到短信验证码
        return res_sms

    def login_admin(self):
        '''
        Mark the sessionid to pass the login authentication, and keep to two hours.
        :return: None
        '''
        sms = self._get_SMS()
        data = {"fun": 4, "phone": self.tel, "pwd": self.pwd, "smscode": sms, "logintype": "admin"}
        response = requests.post(url=self.my_url, data=data, headers=header)
        results = '登录成功 ^_^' if response.json()['ack'] == '0' else '登陆失败 -_-'
        return results
